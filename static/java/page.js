var itemView = document.getElementById("itemview")
var sidemenu = document.getElementById("sidemenu")
var layout = document.getElementById("layout")
var searchBar = document.getElementById("searchbar")


function ShowBackground(){
    itemView.style.visibility = "hidden"
    sidemenu.style.filter = "none"
    layout.style.filter = "none"
    searchBar.style.filter = "none"
}

document.getElementById("close").addEventListener("click", function(){
    ShowBackground()
})

if (document.cookie.includes("email")){
    let uploadLink = document.getElementById("upload")
    let logout = document.getElementById("Logout")

    uploadLink.onclick = () => window.location.href = "/upload"
    logout.onclick = () => window.location.href = "/logout"
}else{
    let signup = document.getElementById("signup")
    let login = document.getElementById("login")

    signup.onclick = () => window.location.href = "/signup"
    login.onclick = () => window.location.href = "/login"
}

ShowBackground()

if (document.cookie.includes("email")){
    let parts = document.cookie.split("; ")
    console.log(parts)
    let loggedIn = parts[2]
    let isLoggedIn = loggedIn.split("=")[1] == "True"

    if (isLoggedIn){
        document.getElementById("welcome").textContent = "Welcome " + parts[1].split("=")[1]
    }
}
/*var items;
fetch("vehicles.json")
.then(response => response.json())
.then(data => {
    items = data
})

for(let i = 0; i < 23; i++){
    let layout = document.getElementById("layout")
    let newButton = document.createElement("button")
    newButton.className = "item"
    newButton.id = i
    layout.appendChild(newButton)

    let image = document.createElement("img")
    let source = "images/" + i+".png"
    image.src = source
    newButton.appendChild(image)

    image.className = "itemImage"

    newButton.onclick = function(){
        ShowItem(i)
    }
}



var itemView = document.getElementById("itemview")
var sidemenu = document.getElementById("sidemenu")
var layout = document.getElementById("layout")
var searchBar = document.getElementById("searchbar")

var login = document.getElementById("login")
var signup = document.getElementById("signup")
var upload = document.getElementById("upload")
var logout = document.getElementById("Logout")

var itemName = document.getElementById("name")
var category = document.getElementById("category")
var desc = document.getElementById("description")
var price = document.getElementById("price")

var closeButton = document.getElementById("close")

function ShowBackground(){
    itemView.style.visibility = "hidden"
    sidemenu.style.filter = "none"
    layout.style.filter = "none"
    searchBar.style.filter = "none"
}


/**
 * @param {number} index - The index of the item to fetch.
 * @returns {Promise<void>}
 */
/*async function ShowItem(index){
    let entry = items[index]
    let name = itemName.querySelector("#custom")
    let cat = category.querySelector("#custom")
    let description = desc.querySelector("#custom")
    let pr = price.querySelector("#custom")
    let img = document.getElementById("itemImage")

    name.textContent = entry.name
    cat.textContent = entry.category
    description.textContent = entry.description
    pr.textContent = "$"+entry.price
    itemView.style.visibility = "visible"
    img.src = "images/" + index+".png"
    sidemenu.style.filter = "blur(10px)"
    layout.style.filter = "blur(10px)"
    searchBar.style.filter = "blur(10px)"
}

closeButton.onclick = ShowBackground
ShowBackground()

login.onclick = () => window.open("login.html","_self")
signup.onclick = () => window.open("signup.html","_self")
upload.onclick = () => window.open("upload.html","_self")

logout.onclick = function(){
    localStorage.setItem("LoggedIn",false)
    window.open("login.html","_self_")
}

if(localStorage.getItem("LoggedIn") == "true"){
    login.style.visibility = "hidden"
    signup.style.visibility = "hidden"
    document.querySelector("#welcome").textContent = "Welcome " + localStorage.getItem("username")
}else{
    console.log("logged out")
    upload.style.visibility = "hidden"
    document.querySelector("#Logout").style.visibility = "hidden"
    document.querySelector("#welcome").style.visibility = "hidden"
}*/