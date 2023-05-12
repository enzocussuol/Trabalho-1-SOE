import { React, useState, useEffect } from 'react';
import Map from './components/Map';
import Avisos from './components/Avisos';

export function App() {
  const [currentExhibitedInfo, setCurrentExhibitedInfo] = useState(0);
  const [dataList, setDataList] = useState([]);
  const [warningsList, setWarningsList] = useState([]);

  function changeCurrentExhibitedInfo(infoNumber) {
    const temperature = document.getElementById("temperature");
    const wind = document.getElementById("wind");
    const uv = document.getElementById("uv");
    const precipitation = document.getElementById("precipitation");
    const avisos = document.getElementById("avisos");

    if (temperature != null && wind != null && uv != null && precipitation != null && avisos != null) {
      temperature.className = "cursor-pointer";
      wind.className = "cursor-pointer";
      uv.className = "cursor-pointer";
      precipitation.className = "cursor-pointer";
      avisos.className = "cursor-pointer";

      if (infoNumber === 0) {
        temperature.className += " text-orange-500";
      } else if (infoNumber === 1) {
        wind.className += " text-orange-500";
      } else if (infoNumber === 2) {
        uv.className += " text-orange-500";
      } else if (infoNumber === 3) {
        precipitation.className += " text-orange-500";
      } else if (infoNumber === 4) {
        avisos.className = " text-orange-500";
      }

      setCurrentExhibitedInfo(infoNumber);
    }
  }

  useEffect(() => {
    const fetchClimateData = async () => {
      const response = await fetch("http://127.0.0.1:30000/clima");
      const dataReturned = await response.json();

      const temperatureData = [['State', 'Temperature']];
      const windData = [['State', 'Wind Speed']];
      const uvData = [['State', 'UV Index']];
      const precipitationData = [['State', 'Precipitation']];

      dataReturned.data.forEach(element => {
        temperatureData.push([element.code, element.data.temperature]);
        windData.push([element.code, element.data.windspeed]);
        uvData.push([element.code, element.data.uv_index_max]);
        precipitationData.push([element.code, element.data.precipitation]);
      });

      const finalList = [];
      finalList.push(temperatureData);
      finalList.push(windData);
      finalList.push(uvData);
      finalList.push(precipitationData);

      setDataList(finalList);
    }

    const fetchWarningsData = async () => {
      const response = await fetch("http://127.0.0.1:30000/avisos");
      const dataReturned = await response.json();

      const list = [];
      dataReturned.forEach(element => {
        list.push({
          code: element.code,
          heat: element.avisos.heat,
          rain: element.avisos.rain,
          change: element.avisos.change
        })
      });

      setWarningsList(list);
    }

    fetchClimateData();
    fetchWarningsData();
  }, []);

  return (
    <div className="w-full font-serif p-5">
      <h1 className="text-center text-2xl">Monitoramento Climático com Kafka</h1>

      <div className="flex justify-around border-b-2 border-black-100 p-2 text-lg mt-5">
        <span id="temperature" className="cursor-pointer text-orange-500" onClick={() => changeCurrentExhibitedInfo(0)}>Temperatura</span>
        <span id="wind" className="cursor-pointer" onClick={() => changeCurrentExhibitedInfo(1)}>Vento</span>
        <span id="uv" className="cursor-pointer" onClick={() => changeCurrentExhibitedInfo(2)}>Índice UV</span>
        <span id="precipitation" className="cursor-pointer" onClick={() => changeCurrentExhibitedInfo(3)}>Precipitação</span>
        <span id="avisos" className="cursor-pointer" onClick={() => changeCurrentExhibitedInfo(4)}>Alertas</span>
      </div>

      {(currentExhibitedInfo >= 0 && currentExhibitedInfo <= 3) ? (
        <Map data={dataList[currentExhibitedInfo]} optionIdx={currentExhibitedInfo} />
      ) : (
        <Avisos dataList={warningsList} />
      )}
    </div>
  );
}

export default App;