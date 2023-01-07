import { Table } from 'react-bootstrap'

const PilotList = ({ data }) => {

    const listPilotData = (pilots) => (
        <div>
            <Table bordered hover>
                <tbody>

                    {pilots.map((item) => {
                        return (
                            <tr>
                                <td>
                                    {Object.keys(item).map((key, index) => {
                                        return (
                                            <div key={item.pilotId + index}>
                                                <p>{key}: {item[key]}</p>
                                            </div>
                                        )
                                    }
                                    )}
                                </td>
                            </tr>
                        )
                    })
                    }
                </tbody>
            </Table>
        </div>
    )

    return (
        <div>
            <h2>Violating Drones:</h2>
            {(!data || data.length === 0)
                ? <div>No data to show.</div>
                : listPilotData(data)}
        </div>
    )
}

export default PilotList
