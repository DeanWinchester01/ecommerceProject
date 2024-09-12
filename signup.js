//buttons
var signupButton = document.getElementById("mainButton")
var loginButton = document.getElementById("secondaryButton")
localStorage.setItem("LoggedIn",false)

//user data

signupButton.onclick = function(){
    let userName = document.getElementById("Username")
    let email = document.getElementById("Email")
    let password = document.getElementById("Password")
    let confirmedPass = document.getElementById("Confirm")
    
    if(userName.value == ""){
        console.log("No username")
        return
    }

    if(!email.value.includes("@gmail.com")){
        console.log("No valid email")
        return
    }

    if(password.value.length < 5 || password.value != confirmedPass.value){
        console.log("password too short or not matching")
        return
    }

    localStorage.setItem("username",userName.value)
    localStorage.setItem("email",email.value)
    localStorage.setItem("password",password.value)
    
    window.open("page.html","_self")
}

loginButton.onclick = function(){
    window.open("login.html","_self")
}