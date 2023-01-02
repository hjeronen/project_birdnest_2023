import { useState, useEffect } from 'react'
import PilotList from './components/PilotList'
import pilotService from './services/pilots'

const App = () => {
  const [pilots, setPilots] = useState([])

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
