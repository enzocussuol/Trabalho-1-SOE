package ufes.kafkastreams;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.utils.Bytes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.errors.StreamsUncaughtExceptionHandler;
import org.apache.kafka.streams.kstream.*;
import org.apache.kafka.streams.state.KeyValueStore;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Properties;

@SpringBootApplication
public class KafkaStreamsApplication {

	public static void main(String[] args) {
		SpringApplication.run(KafkaStreamsApplication.class, args);

		String BootstrapServer = "localhost:9092";

		Properties config = new Properties();
		config.put(StreamsConfig.APPLICATION_ID_CONFIG, "weather-java");
		config.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, BootstrapServer);
		config.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
		config.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
		config.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

		StreamsBuilder builder = new StreamsBuilder();

		/**
		 * Temperatura alta e alto indice UV (Passe protetor e procure ficar na sombra)
		 */
		KStream<String, String> tempInput = builder.stream("temperature");
		KStream<String, String> uvInput = builder.stream("uv");

		ValueJoiner<String, String, Boolean> highUVandTemp = (leftValue, rightValue) -> Float.parseFloat(leftValue) >= 30 || Float.parseFloat(rightValue) >= 6;
		tempInput.join(uvInput,highUVandTemp,JoinWindows.of(Duration.ofSeconds(2)))
				.peek((key,value) -> System.out.println("[Join] key: " + key + " value: " + value))
				.mapValues(Object::toString)
				.to("heat");

		/**
		 * Chuva e Vento (Se agaselhe e evite sair na rua)
		 */
		KStream<String, String> windInput = builder.stream("wind");
		KStream<String, String> precInput = builder.stream("precipitation");

		ValueJoiner<String, String, Boolean> windAndPrec = (leftValue, rightValue) -> Float.parseFloat(leftValue) >= 8 && Float.parseFloat(rightValue) >= 50;
		windInput.join(precInput,windAndPrec,JoinWindows.of(Duration.ofSeconds(2)))
				.peek((key,value) -> System.out.println("[Join] key: " + key + " value: " + value))
				.mapValues(Object::toString)
				.to("rain");

		/**
		 * Variação brusca de temperatura 5 graus em 1 hora
		 */
		Aggregator<String, String, ArrayList<String>> agg = (location, temp, hist) -> {
			hist.add(temp);
			return hist;
		};

		KTable<String, ArrayList<String>> locationsTempHist = tempInput
				.groupByKey()
				.aggregate(() -> new ArrayList<String>(), agg, Materialized.<String, ArrayList<String>, KeyValueStore<Bytes, byte[]>> as("store_locations_temp")
						.withKeySerde(Serdes.String())
						.withValueSerde(new Serdes.ListSerde(ArrayList.class, Serdes.String())));


		locationsTempHist
				.mapValues(value -> {
					if (value.size() <= 1) return "0";

					Float currentTemp = Float.parseFloat(value.get(value.size() - 1));
					Float lastTemp = Float.parseFloat(value.get(value.size() - 2));

					if (currentTemp - lastTemp >= 5) return "1";
					else if (currentTemp - lastTemp < -5) return "-1";

					return "0";
				})
				.toStream()
				.to("change");

		KafkaStreams streams = new KafkaStreams(builder.build(), config);

		streams.setUncaughtExceptionHandler(ex -> {
			System.out.println("Kafka-Streams uncaught exception occurred. Stream will be replaced with new thread"+ ex);
			return StreamsUncaughtExceptionHandler.StreamThreadExceptionResponse.REPLACE_THREAD;
		});

		// only do this in dev - not in prod
		streams.cleanUp();
		streams.start();
		// print the topology
		//streams.localThreadsMetadata().forEach(data -> System.out.println(data));
		streams.metadataForLocalThreads().forEach (System.out::println);

		// shutdown hook to correctly close the streams application
		Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
		System.out.println("Streams começo");
	}
}
