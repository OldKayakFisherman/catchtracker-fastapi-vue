
export default class StatAPIService
{
    getStats() {

        axios({
            method:'post',
            url:'logout',
            baseURL: '/stats',
           })
           .then(response => {
              return response.data;
           })
           .catch(error => {
               return -1;
           });    
    }
}

