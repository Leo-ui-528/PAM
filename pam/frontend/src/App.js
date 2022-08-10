




const axios = require('axios').default;


    axios
        .get("http://127.0.0.1:8000/api/employee/")
        .then( response =>{
             console.log(response.data);
        })
        .catch((error) => {
            console.error(error);
        });

    
    


