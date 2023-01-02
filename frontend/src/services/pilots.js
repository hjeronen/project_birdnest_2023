import axios from 'axios'

const baseURL = 'http://localhost:8000/api/'

const getPilots = async props => {
    const response = await axios.get(baseURL + 'pilots/')
    return response.data
}

const functions = {
    getPilots
}

export default functions