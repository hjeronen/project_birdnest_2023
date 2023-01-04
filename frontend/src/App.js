import { useState, useEffect } from 'react'
import PilotList from './components/PilotList'
import pilotService from './services/pilots'
import { w3cwebsocket as W3CWebSocket } from "websocket";

const App = () => {
  const [pilots, setPilots] = useState([])
  const ticksSocket = new W3CWebSocket('ws://' + window.location.host + '/ws/backend/pilot_list/')

  ticksSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log('data', data);
      // do whatever required with received data ...
  }

  useEffect(() => {
    pilotService
      .getPilots()
      .then(pilots => setPilots(pilots))
      .catch(error => setPilots([]))
  }, [])

  return (
    <div>
      <PilotList pilots={pilots} />
    </div>
  )
}

export default App
