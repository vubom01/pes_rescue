async function getUser(event) {
    event.preventDefault();
    // Default options are marked with *
    let url = 'http://127.0.0.1:8000/login';
    let data = {
        username: "test",
        password: "test"
    }

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    console.log(response);
}


let button = document.getElementById('login-button')
button.addEventListener('click', getUser);