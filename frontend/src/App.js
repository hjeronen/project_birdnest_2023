import { useState, useEffect } from 'react'
import PilotList from './components/PilotList'
import pilotService from './services/pilots'
// import { w3cwebsocket as W3CWebSocket } from "websocket";

const App = () => {
  const [pilots, setPilots] = useState([])
  const [data, setData] = useState([{test: "test"}])

  useEffect(() => {
    pilotService
      .getPilots()
      .then(pilots => setPilots(pilots))
      .catch(error => setPilots([]))

      const ws = new WebSocket('ws://localhost:8000/ws/backend/pilot_list/')

      ws.onmessage = (event) => {
        const json = JSON.parse(event.data)
        try {
          if ((json.event = "data")) {
            setData(json.data)
          }
        } catch (err) {
          console.log(err)
        }
      }
  }, [])

  const showData = () => {
    return (
      <div>
        {data &&
          data.map(
            item => Object.keys(item).map(
              key => {
                return (
                <div>
                  <p>{key}: {item[key]}</p>
                </div>
                )}))
          }
      </div>
    )
  }

  return (
    <div>
      <PilotList pilots={pilots} />
      <h3>Test data</h3>
      <div>
        {data ? showData() : <div></div>}
      </div>
    </div>
  )
}

export default App
