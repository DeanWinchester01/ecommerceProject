document.getElementById('mainButton').onclick = function() {
    console.log("hi")
    email = document.getElementById('email').value;
    password = document.getElementById('password').value;
    
    if (localStorage.getItem('email') != email) {
        alert("ERROR: Wrong email address!");
        return;
    }
    if (localStorage.getItem('password') != password) {
        alert("ERROR: Wrong password!");
        return;
    }

    window.open("page.html");
}
