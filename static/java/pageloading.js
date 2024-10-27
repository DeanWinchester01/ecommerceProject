var itemView = document.getElementById("itemview")
var sidemenu = document.getElementById("sidemenu")
var layout = document.getElementById("layout")
var searchBar = document.getElementById("searchbar")

var itemName = document.getElementById("name")
var category = document.getElementById("category")
var desc = document.getElementById("description")
var price = document.getElementById("price")
let tags = document.getElementById("tags")

let uploadLink = document.getElementById("upload")
let mainLink = document.getElementById("mainPage")
let logout = document.getElementById("Logout")

var cookies = document.cookie.split(";");
let username = cookies[1].split("=")[1]
let email = cookies[0].split("=")[1]
document.getElementById("welcome").textContent = "Welcome " + cookies[1].split("=")[1]

function ShowBackground(){
    itemView.style.visibility = "hidden"
    sidemenu.style.filter = "none"
    layout.style.filter = "none"
    searchBar.style.filter = "none"
}
document.getElementById("close").addEventListener("click", function(){
    ShowBackground()
})


uploadLink.onclick = () => window.location.href = "/upload"
logout.onclick = () => window.location.href = "/logout"
//mainLink.onclick = () => window.location.href = "/page"

/**
 * @param {Array} vehicleList 
 */
function ShowVehicles(vehicleList){
    vehicleList.forEach(function(vehicle){
        let button = document.createElement("button")
        button.id = vehicle["_id"]
        button.className = "item"

        let image = document.createElement("img")
        image.className = "itemImage"
        console.log(vehicle["_id"])
        image.src = "/static/images/"+vehicle["_id"]+".png"

        let priceElement = document.createElement("div");
        priceElement.className = "itemPrice";
        let formattedPrice;
        if (vehicle.price % 1 === 0) 
            formattedPrice = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(vehicle.price);
         else 
            formattedPrice = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(vehicle.price);
        
        priceElement.textContent = formattedPrice;
        /*priceElement.textContent = "$" + vehicle.price;*/

        let nameElement = document.createElement("div")
        nameElement.className = "itemName"
        nameElement.textContent = vehicle.name || vehicle.vehicle;

        button.appendChild(image)
        button.appendChild(priceElement)
        button.appendChild(nameElement)
        layout.appendChild(button)

        button.onclick = function(){
            ShowItem(vehicle)
        }
    })
}

function ShowItem(vehicle){
    let name = itemName.querySelector("#custom")
    let cat = category.querySelector("#custom")
    let description = desc.querySelector("#custom")
    let pr = price.querySelector("#custom")
    let img = document.getElementById("itemImage")
    let tag = tags.querySelector("#custom")

    name.textContent = Object.keys(vehicle, "vehicle") && vehicle.vehicle || vehicle.name
    cat.textContent = vehicle.category
    description.textContent = vehicle.description
    pr.textContent = "$"+vehicle.price
    itemView.style.visibility = "visible"
    img.src = "/static/images/" + vehicle["_id"]+".png"
    tag.textContent = vehicle.tags
    sidemenu.style.filter = "blur(10px)"
    layout.style.filter = "blur(10px)"
    searchBar.style.filter = "blur(10px)"
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

function Search(vehicles){
    let buttons = document.getElementsByClassName("item")
    for(let i = buttons.length-1; i >= 0; i--){
        buttons[i].remove()
    }
    console.log(vehicles)
    ShowVehicles(vehicles)
}

/**
 * 
 * @param {Array} ids 
 */
function GetVehicles(ids){
    let searchvehicles = []
    for(let vehicle = 0; vehicle < vehicles.length; vehicle++){
        if(ids.includes(vehicles[vehicle]["_id"])){
            searchvehicles.push(vehicles[vehicle])
        }
    }

    Search(searchvehicles)
}

searchBar.addEventListener("input",function(){
    //Search(searchBar.value)
    let search = JSON.stringify(searchBar.value)
    fetch("/search",{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(search)
    }).then(response =>{
        //console.log(response)
        if(!response.ok){
            throw new Error("HTTP error! status: "+response.status)
        }
        return response.json()
    }).then(data =>{
        console.log(data)
        GetVehicles(data)
        //vehicles = data
        //ShowVehicles(vehicles)
        //console.log(typeof(data))
    }).catch(error => console.log(error))
})

var vehicles = []
