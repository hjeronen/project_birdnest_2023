import { useState, useEffect } from 'react'
import { Container, Col, Row, Navbar, Spinner } from 'react-bootstrap'
import PilotList from './components/PilotList'
import pilotService from './services/pilots'

import 'bootstrap/dist/css/bootstrap.min.css'

const App = () => {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    setLoading(true)

    pilotService
      .getPilots()
      .then(pilots => {
        setData(pilots)
        setLoading(false)
      })
      .catch(error => {
        setData([])
        setLoading(false)
      })

    const ws = new WebSocket('ws://' + window.location.host + process.env.REACT_APP_WS_URL)

    ws.onmessage = (event) => {
      // string to object
      const json = JSON.parse(event.data)
      try {
        const newData = json.data
        setData(newData)
      } catch (err) {
        console.log(err)
      }
    }

  }, [])

  const showSpinner = () => (
    <div>
      <p>Loading data...</p>
      <Spinner animation="border" variant="info" />
    </div>
  )

  return (
    <div>
      <Navbar bg="dark">
        <Container>
          <Navbar.Brand style={{ color: 'white' }}>Project Birdnest 2023</Navbar.Brand>
        </Container>
      </Navbar>
      <Container>
        <Row>
          <Col>
            {loading
              ? showSpinner()
              : <PilotList data={data} />
            }
          </Col>
        </Row>
      </Container>
    </div>
  )
}

export default App
