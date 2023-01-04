const PilotList = ({ pilots }) => {
    return (
        <div>
            <h2>Violating Drones:</h2>
            {
                pilots
                    ? pilots.map(pilot => (
                        <div>
                            <p>{pilot.pilotId}</p>
                            <p>{pilot.firstName}</p>
                            <p>{pilot.lastName}</p>
                            <p>{pilot.phoneNumber}</p>
                            <p>{pilot.createdDt}</p>
                            <p>{pilot.email}</p>
                            <p>{pilot.closest_distance}</p>
                            <p>{pilot.last_seen}</p>
                        </div>
                    ))
                    : <p>No pilots to show.</p>
            }
        </div>
    )
}

export default PilotList
