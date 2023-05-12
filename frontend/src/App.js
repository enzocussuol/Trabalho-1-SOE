import { React, useState, useEffect } from 'react';
import { Chart } from 'react-google-charts';

export const options = {
  region: "BR",
  colorAxis: {
    colors: ["blue", "aqua", "green", "yellow", "orange", "red"],
    values: [0, 35]
  },
  resolution: 'provinces',
  backgroundColor: "",
  datalessRegionColor: "#123456",
  defaultColor: "#f5f5f5"
};

export function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:30000/clima");

      const json = await response.json();
      console.log(json)

      const list = [['State', 'Temperature']];
      json.data.map((element) => {
        list.push([element.code, element.data.temperature])
      })

      setData(list);
    }

    fetchData();
  }, [])

  return (
    <div className="w-full h-screen flex justify-center">
      <div className="self-center">
        <Chart
          chartType="GeoChart"
          data={data}
          options={options}
        />
      </div>
    </div>
  );
}

export default App;