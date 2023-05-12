import { React } from 'react';

function Avisos({ dataList }) {
    return (
        <>
            <table className="w-full text-xl text-center mt-5">
                <thead>
                    <tr>
                        <th>UF</th>
                        <th>☀️ ➡️ 🧴</th>
                        <th>💨☔ ➡️ 🧣</th>
                        <th>🥵 🔃 🥶</th>
                    </tr>
                </thead>
                <tbody>
                    {dataList.map((data, index) => (
                        <tr key={index}>
                            <td>{data.code}</td>
                            <td>{data.heat ? "☀️" : "⛅"}</td>
                            <td>{data.rain ? "☔" : "🌂"}</td>
                            <td>{data.change == -1 ? "⬇️" : data.change == 1 ? "⬆️" : "↔" }</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    );
}

export default Avisos;