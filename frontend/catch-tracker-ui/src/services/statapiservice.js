import axios from "axios";

export default 
{
    getStats(callback) {
       
        return axios.get('http://localhost:5000/api/v1/stats').then((response) => {
            return response.data;
        });
    }

}
