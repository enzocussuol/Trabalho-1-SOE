import { React, useState, useEffect } from 'react';
import { Chart } from 'react-google-charts';

// export const data = [
//   ['State', 'Views'],
//   ['BR-AC', 3400],
//   ['BR-AL', 300],
//   ['BR-AP', 300],
//   ['BR-AM', 321],
//   ['BR-BA', 300],
//   ['BR-CE', 300],
//   ['BR-ES', 300],
//   ['BR-GO', 300],
//   ['BR-MA', 300],
//   ['BR-MT', 300],
//   ['BR-MS', 300],
//   ['BR-MG', 300],
//   ['BR-PA', 32],
//   ['BR-PB', -21],
//   ['BR-PR', 3320],
//   ['BR-PE', 300],
//   ['BR-PI', 300],
//   ['BR-RJ', 300],
//   ['BR-RN', 300],
//   ['BR-RS', 300],
//   ['BR-RO', 300],
//   ['BR-RR', 300],
//   ['BR-SC', 300],
//   ['BR-SP', 300],
//   ['BR-SE', 300],
//   ['BR-TO', 300],
//   ['BR-DF', 4231]
// ];

export const options = {
  region: "BR",
  colorAxis: { colors: ["#00853f", "black", "#e31b23"] },
  resolution: 'provinces',
  backgroundColor: "",
  datalessRegionColor: "#123456",
  defaultColor: "#f5f5f5"
};

export function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("https://179.234.237.25:8000/", {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      });

      console.log(response);

      const json = await response.json();

      console.log(json);

      setData(json.data);
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