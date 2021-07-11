async function getValidUser(event, username, password) {
    event.preventDefault();
    // Default options are marked with *
    let url = 'http://127.0.0.1:8000/login';
    let data = {
        username: username,
        password: password
    }
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      if(response.ok) {
        const jsonResponse = await response.json();
        // console.log(jsonResponse)
        return jsonResponse;
      }
    }
    catch(e) {
      console.log(e);
    }
    
}

const acceptLogin = (responseStatus, username) => {
  if(responseStatus.status) {
    localStorage.setItem('username', username)
    window.open('/gui/html/profile.html', '_self')
  }
}

const loginForm = document.getElementById('login-form')

let responseStatus;
loginForm.addEventListener('submit',async (event) => {
  event.preventDefault()
  const username = document.querySelector('#your_name').value
  const password = document.querySelector('#your_pass').value
  responseStatus = await getValidUser(event, username, password);
  acceptLogin(responseStatus, username)
});

