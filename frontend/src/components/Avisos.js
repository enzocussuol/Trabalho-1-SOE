import { React } from 'react';

function Avisos({ dataList }) {
    return (
        <>
            <div className="overflow-y-auto h-96">
                <table className="w-full text-xl text-center mt-5">
                    <thead>
                        <tr>
                            <th>UF</th>
                            <th>☀️ ➡️ 🧴</th>
                            <th>💨☔ ➡️ 🧣</th>
                            <th>🥵 🔃 🥶</th>
                            <th>📈</th>
                        </tr>
                    </thead>
                    <tbody>
                        {dataList.map((data, index) => (
                            <tr key={index}>
                                <td>{data.code}</td>
                                <td>{data.heat ? "☀️" : "⛅"}</td>
                                <td>{data.rain ? "☔" : "🌂"}</td>
                                <td>{data.change === -1 ? "⬇️" : data.change === 1 ? "⬆️" : "↔"}</td>
                                <td>{(Math.round(data.avg * 100) / 100).toFixed(2)}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="text-xl py-10">
                <h2>Legenda:</h2>
                <p>☀️ ➡️ 🧴: Temperatura alta e alto indice UV (Passe protetor e procure ficar na sombra)</p>
                <p>💨☔ ➡️ 🧣: Chuva e Vento (Se agaselhe e evite sair na rua)</p>
                <p>🥵 🔃 🥶: Variação brusca de temperatura 5 graus em 1 hora</p>
                <p>📈: Média de Temperatura</p>
            </div>
        </>
    );
}

export default Avisos;