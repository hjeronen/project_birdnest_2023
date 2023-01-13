import axios from 'axios'

const baseURL = process.env.REACT_APP_API_URL ? process.env.REACT_APP_API_URL : ''

const getPilots = async props => {
    const response = await axios.get(baseURL + '/api/pilots/')
    return response.data
}

const functions = {
    getPilots
}

export default functions