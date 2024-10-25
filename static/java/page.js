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

ShowBackground()
document.getElementById("close").addEventListener("click", function(){
    ShowBackground()
})

if (document.cookie.includes("email")){
    let uploadLink = document.getElementById("upload")
    let userLink = document.getElementById("uploads")
    let logout = document.getElementById("Logout")

    var cookies = document.cookie;
    let username = cookies.split("; ")[1].split("=")[1];

    uploadLink.onclick = () => window.location.href = "/upload"
    logout.onclick = () => window.location.href = "/logout"
    userLink.onclick = () => window.location.href = "/page/"+username
}else{
    let signup = document.getElementById("signup")
    let login = document.getElementById("login")

    signup.onclick = () => window.location.href = "/signup"
    login.onclick = () => window.location.href = "/login"
}


if (document.cookie.includes("email")){
    let parts = document.cookie.split("; ")
    console.log(parts)
    let loggedIn = parts[2]
    let isLoggedIn = loggedIn.split("=")[1] == "True"

    if (isLoggedIn){
        document.getElementById("welcome").textContent = "Welcome " + parts[1].split("=")[1]
    }
}

/**
 * @param {Array} vehicleList 
 */
function ShowVehicles(vehicleList){
    let index = 0
    vehicleList.forEach(function(vehicle){
        let button = document.createElement("button")
        button.id = vehicle["_id"]
        button.className = "item"

        let image = document.createElement("img")
        image.className = "itemImage"
        image.src = "static/images/"+vehicle["_id"]+".png"

        let priceElement = document.createElement("div");
        priceElement.className = "itemPrice";
        let formattedPrice;
        if (vehicle.price % 1 === 0) {
            formattedPrice = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(vehicle.price);
        } else {
            formattedPrice = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(vehicle.price);
        }
        priceElement.textContent = formattedPrice;
        /*priceElement.textContent = "$" + vehicle.price;*/

        let nameElement = document.createElement("div")
        nameElement.className = "itemName"
        nameElement.textContent = vehicle.name || vehicle.vehicle;

        button.appendChild(image)
        button.appendChild(priceElement)
        button.appendChild(nameElement)
        layout.appendChild(button)

        let i = index
        button.onclick = function(){
            console.log(i)
            ShowItem(vehicle)
        }
        index++
    })
}


function ShowItem(vehicle) {
    let name = document.querySelector("#name-custom");
    let cat = document.querySelector("#category-custom");
    let description = document.querySelector("#description-custom");
    let pr = document.querySelector("#price-custom");
    let img = document.getElementById("itemImage");
    let tag = document.querySelector("#tags-custom");

    name.textContent = Object.keys(vehicle, "vehicle") && vehicle.vehicle || vehicle.name;
    cat.textContent = vehicle.category;
    description.textContent = vehicle.description;
    pr.textContent = "$" + vehicle.price;
    img.src = "static/images/" + vehicle["_id"] + ".png";
    tag.textContent = vehicle.tags;

    itemView.style.visibility = "visible";
    sidemenu.style.filter = "blur(10px)";
    layout.style.filter = "blur(10px)";
    searchBar.style.filter = "blur(10px)";
}


/**
 * 
 * @param {String} name
 * @returns {Array}
 */
function GetVehiclesByName(name){
    let allCurrentVehicles = vehicles
    if(name == ""){
        console.log("returned all vehicles")
        return allCurrentVehicles
    }

    let newList = []

    for(let i = 0; i < allCurrentVehicles.length; i++){
        let vehicle = allCurrentVehicles[i]
        let vehicleName = Object.keys(vehicle).includes("vehicle") && vehicle.vehicle || vehicle.name
        
        if(vehicleName.toLowerCase().includes(name)){
            newList.push(vehicle)
        }
    }
    console.log("returned new list")
    return newList
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

    let newList = []

    console.log(tags)
    for(let vehicle = vehicles.length-1; vehicle >= 0; vehicle--){
        let currentVehicle = vehicles[vehicle]
        if(!Object.keys(currentVehicle).includes("tags")) continue
        for(let tag = 0; tag < tags.length; tag++){
            console.log("searching tag: "+tags[tag])
            if(!currentVehicle.tags.includes(tags[tag])){
                allCurrentVehicles.slice(vehicle,vehicle+1)
                console.log(allCurrentVehicles)
            }else{
                newList.push(currentVehicle)
                console.log("vehicle "+vehicle+" includes "+tags[tag])
                break
            }
        }
    }

    return newList
}

/**
 * 
 * @param {string} search 
 * @returns {Array}
 */
function SearchForVehicles(search){
    let searchParameters = search.split(" ")
    let vehicleName = "";
    let tags = []
    for(let i = 0; i < searchParameters.length; i++){
        let param = searchParameters[i].toLowerCase()
        if (param[0] == "#" && param.length > 1){
            tags.push(param)
            console.log("pushed tag")
        }

        if(!param.includes("#") && vehicleName == ""){
            console.log(param)
            vehicleName = param.toLowerCase()
        }
    }

    let list = GetVehiclesByName(vehicleName)
    console.log(list)
    let newList = GetVehiclesByTag(list, tags)
    console.log(newList)
    return newList
}

function Search(searchText){
    let vehicles = SearchForVehicles(searchText)
    let buttons = document.getElementsByClassName("item")
    for(let i = buttons.length-1; i >= 0; i--){
        buttons[i].remove()
    }
    console.log(vehicles)
    ShowVehicles(vehicles)
}

searchBar.addEventListener("input",function(){
    Search(searchBar.value)
    /*let searchParameters = searchBar.value

    let vehicles = SearchForVehicles(searchParameters)
    let buttons = document.getElementsByClassName("item")
    for(let i = buttons.length-1; i >= 0; i--){
        buttons[i].remove()
    }
    console.log(vehicles)
    ShowVehicles(vehicles)*/
})

var vehicles = []
fetch('/page/getdata/vehicles_temp')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        vehicles = data
        ShowVehicles(vehicles)
    })
    .catch(error => console.error('Fetch error:', error));

var used = document.getElementById("used")
var cylinder = document.getElementById("cylinder")
var speed = document.getElementById("speed")
var medium = document.getElementById("medium")
var chrissy = document.getElementById("chrissy")

function GetFilters(){
    let filters = ""
    console.log(used.checked)
    if(used.checked)
        filters += "#slightlyused "

    if(cylinder.checked)
        filters += "#4cylinder "

    if(speed.checked)
        filters += "#200km "

    if(medium.checked)
        filters += "#4seater "

    if(chrissy.checked)
        filters += "#sexy "

    filters += searchBar.value
    Search(filters)
}

used.onclick = GetFilters
cylinder.onclick = GetFilters
speed.onclick = GetFilters
medium.onclick = GetFilters
chrissy.onclick = GetFilters