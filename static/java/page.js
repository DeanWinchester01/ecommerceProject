var itemView = document.getElementById("itemview")
var sidemenu = document.getElementById("sidemenu")
var layout = document.getElementById("layout")
var searchBar = document.getElementById("searchbar")

var itemName = document.getElementById("name")
var category = document.getElementById("category")
var desc = document.getElementById("description")
var price = document.getElementById("price")
let tags = document.getElementById("tags")

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
var vehicles = []
fetch('/page/getdata')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        vehicles = data
        console.log(vehicles)
    })
    .catch(error => console.error('Fetch error:', error));

var buttons = document.getElementsByClassName("item")
for (let i = 0; i < buttons.length; i++){
    let button = buttons[i]
    button.onclick = function(){
        ShowItem(i)
    }
};

/**
 * 
 * @param {Number} index 
 */
function ShowItem(index){
    let entry = vehicles[index]
    let name = itemName.querySelector("#custom")
    let cat = category.querySelector("#custom")
    let description = desc.querySelector("#custom")
    let pr = price.querySelector("#custom")
    let img = document.getElementById("itemImage")
    let tag = tags.querySelector("#custom")

    name.textContent = entry.vehicle
    cat.textContent = entry.category
    description.textContent = entry.description
    pr.textContent = "$"+entry.price
    itemView.style.visibility = "visible"
    img.src = "static/images/" + index+".png"
    tag.textContent = entry.tags
    sidemenu.style.filter = "blur(10px)"
    layout.style.filter = "blur(10px)"
    searchBar.style.filter = "blur(10px)"
}

/**
 * 
 * @param {Array} parameters
 * @returns {Array}
 */
function GetVehiclesByName(name){
    let allCurrentVehicles = vehicles
    if(name.length == 0)
        return allCurrentVehicles

    let newList = []

    for(let i = 0; i < allCurrentVehicles.length; i++){
        let vehicle = allCurrentVehicles[i]
        if(!Object.keys(vehicle).includes("vehicle")) continue
        
        if(vehicle.vehicle.toLowerCase().includes(name)){
            newList.push(vehicle)
        }
    }
}

/**
 * 
 * @param {Array} vehicles 
 * @param {Array} tags 
 * @returns {Array} 
 */
function GetVehiclesByTag(vehicles, tags){
    let allCurrentVehicles = vehicles
    if(tags.length == 0)
        return allCurrentVehicles

    for(let vehicle = vehicles.length-1; vehicle >= 0; vehicle--){
        let currentVehicle = vehicles[vehicle]
        if(!Object.keys(currentVehicle).includes("tags")) continue
        for(let tag = 0; tag < tags.length; tag++){

            if(!currentVehicle.tags.includes(tags[tag]))
                allCurrentVehicles.slice(vehicle,1)
        }
    }

    return allCurrentVehicles
}

searchBar.addEventListener("input",function(){
    let searchParameters = searchBar.value.split(" ")
    console.log(searchBar.value)

    let vehicleName = "";
    let tags = []
    for(let i = 0; i < searchParameters.length; i++){
        let param = searchParameters[i].toLowerCase()
        console.log(param)
        if (param.includes("#") && param.length > 1){
            tags.push(param)
        }else{
            vehicleName = param.toLowerCase()
        }
    }

    let list = GetVehiclesByName(vehicleName)
    let newList = GetVehiclesByTag(list, tags)
    console.log(newList)
})