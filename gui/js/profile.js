const username = localStorage.getItem('username')
const logoutButton = document.querySelector('#logout-button')
let viewUsername = document.querySelector('h1')
viewUsername.innerHTML += username;
logoutButton.addEventListener('click', () => {
  localStorage.removeItem('username')
  window.open('/gui/html/loginsignup.html', '_self')
})
