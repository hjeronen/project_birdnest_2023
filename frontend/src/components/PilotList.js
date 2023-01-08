import { Card, ListGroup } from 'react-bootstrap'

const PilotList = ({ data }) => {

    const listPilotData = (pilots) => (
        <div>
            {pilots.map(pilot => {
                return (
                    <Card key={pilot.pilotId}>
                        <Card.Body>
                            <Card.Title>
                                {pilot.firstName} {pilot.lastName}
                            </Card.Title>
                            <ListGroup variant="flush">
                                <ListGroup.Item>
                                    Email: {pilot.email}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    Phone: {pilot.phoneNumber}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    Drone serial nr: {pilot.drone_serial_number}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    Closest distance: {
                                        Math.round(pilot.closest_distance / 100) / 10
                                    } meters
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    Last seen: {pilot.last_seen}
                                </ListGroup.Item>
                            </ListGroup>
                        </Card.Body>
                    </Card>
                )
            })}
        </div>
    )

    return (
        <div>
            <h3>Pilots of the Drones Violating the NDZ:</h3>
            {(!data || data.length === 0)
                ? <div>No data to show.</div>
                : listPilotData(data)}
        </div>
    )
}

export default PilotList
