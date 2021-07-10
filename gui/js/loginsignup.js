
async function getUser(event) {
    event.preventDefault();
    // Default options are marked with *
    let url = 'http://127.0.0.1:8000/login';
    let data = `{
        "username": "test", 
        "password": "test"
    }`
    
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'no-cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      header: { 'Content-Type' : 'application/json' },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.parse(data) // body data type must match "Content-Type" header
    });
    console.log(response) ; // parses JSON response into native JavaScript objects
  }
  

let button = document.getElementById('login-button')
button.addEventListener('click', getUser);