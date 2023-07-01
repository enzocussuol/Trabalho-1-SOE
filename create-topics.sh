#!/bin/bash

kafka-topics.sh --create --topic clima --bootstrap-server localhost:9092
kafka-topics.sh --create --topic temperature --bootstrap-server localhost:9092
kafka-topics.sh --create --topic wind --bootstrap-server localhost:9092
kafka-topics.sh --create --topic uv --bootstrap-server localhost:9092
kafka-topics.sh --create --topic precipitation --bootstrap-server localhost:9092
kafka-topics.sh --create --topic avisos --bootstrap-server localhost:9092