import { React } from 'react';
import { Chart } from 'react-google-charts';

export const options = [
    {
        region: "BR",
        colorAxis: {
            colors: ["blue", "aqua", "green", "yellow", "orange", "red"],
            values: [0, 35]
        },
        resolution: 'provinces',
        backgroundColor: "",
        datalessRegionColor: "#123456",
        defaultColor: "#f5f5f5",
        width: 1000,
        height: 600
    },
    {
        region: "BR",
        colorAxis: {
            colors: ["gold", "yellow", "cyan", "cornflowerblue", "blue", "darkblue"],
            values: [0, 50]
        },
        resolution: 'provinces',
        backgroundColor: "",
        datalessRegionColor: "#123456",
        defaultColor: "#f5f5f5",
        width: 1000,
        height: 600
    },
    {
        region: "BR",
        colorAxis: {
            colors: ["green", "yellow", "orange", "red", "purple"],
            values: [1, 11]
        },
        resolution: 'provinces',
        backgroundColor: "",
        datalessRegionColor: "#123456",
        defaultColor: "#f5f5f5",
        width: 1000,
        height: 600
    },
    {
        region: "BR",
        colorAxis: {
            colors: ["whitesmoke", "gainsboro", "cyan", "cornflowerblue", "blue", "darkblue"],
            values: [0, 100]
        },
        resolution: 'provinces',
        backgroundColor: "",
        datalessRegionColor: "#123456",
        defaultColor: "#f5f5f5",
        width: 1000,
        height: 600
    }
];

function Map({ data, optionIdx }) {
    return (
        <div className="flex justify-center">
            <Chart
                chartType="GeoChart"
                data={data}
                options={options[optionIdx]}
            />
        </div>
    )
}

export default Map;