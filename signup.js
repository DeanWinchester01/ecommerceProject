//buttons
var signupButton = document.getElementById("mainButton")
var loginButton = document.getElementById("secondaryButton")

//user data

signupButton.onclick = function(){
    var userName = document.getElementById("Username")
    var email = document.getElementById("Email")
    var password = document.getElementById("Password")
    var confirmedPass = document.getElementById("Confirm")
    
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
    
    window.open("page.html")
}

loginButton.onclick = function(){
    window.open("login.html")
}