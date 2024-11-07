var itemView = document.getElementById("itemview")
var sidemenu = document.getElementById("sidemenu")
var layout = document.getElementById("layout")
var searchBar = document.getElementById("searchbar")
var filterview = document.getElementById("filterview")

var itemName = document.getElementById("name")
var category = document.getElementById("category")
var desc = document.getElementById("description")
var price = document.getElementById("price")
let tags = document.getElementById("tags")

//let uploadLink = document.getElementById("upload")
//let mainLink = document.getElementById("mainPage")
//let logout = document.getElementById("Logout")

var cookies = document.cookie.split(";");
let username = cookies[1].split("=")[1]
let email = cookies[0].split("=")[1]
document.getElementById("welcome").textContent = cookies[1].split("=")[1]

function ShowBackground(){
    itemView.style.visibility = "hidden"
    sidemenu.style.filter = "none"
    layout.style.filter = "none"
    searchBar.style.filter = "none"
    filterview.style.filter = "none"
}

/**
 * @param {Array} vehicleList 
 */
function ShowVehicles(vehicleList) {
    vehicleList.forEach(function(vehicle) {
        let div = document.createElement("div")
        div.className = "item"
        div.id = vehicle["_id"]

        let button = document.createElement("button");
        button.id = vehicle["_id"];
        button.className = "item";

        console.log(window.location.href.length)
        if(window.location.href.length > 26){
            let del = document.createElement("button");
            del.className = "delete"
            div.append(del)

            del.onclick = function(){
                window.location.href = "/delete/"+vehicle["_id"]
            }
        }

        let image = document.createElement("img");
        image.className = "itemImage";
        console.log(vehicle["_id"]);
        image.src = "/static/images/" + vehicle["_id"] + ".png";

        let nameElement = document.createElement("div");
        nameElement.className = "itemName";
        nameElement.textContent = vehicle.name || vehicle.vehicle;

        let priceElement = document.createElement("div");
        priceElement.className = "itemPrice";
        let formattedPrice;
        if (vehicle.price % 1 === 0)
            formattedPrice = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(vehicle.price);
        else
            formattedPrice = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(vehicle.price);

        priceElement.textContent = formattedPrice;

        // Append name first, then price
        button.appendChild(image);
        button.appendChild(nameElement);
        button.appendChild(priceElement);
        div.appendChild(button);
        layout.appendChild(div)
        

        button.onclick = function() {
            ShowItem(vehicle);
        };
    });
}

function ShowItem(vehicle) {
    let name = document.getElementById("name-custom") || document.getElementById("name");
    let cat = document.getElementById("category-custom") || document.getElementById("category");
    let description = document.getElementById("description-custom") || document.getElementById("description");
    let pr = document.getElementById("price-custom") || document.getElementById("price");
    let img = document.getElementById("itemImage");
    let tag = document.getElementById("tags-custom") || document.getElementById("tags");

    name.textContent = vehicle.vehicle || vehicle.name || "Unknown Vehicle";
    cat.textContent = vehicle.category || "Uncategorized";
    description.textContent = vehicle.description || "No description available";
    pr.textContent = "$" + (vehicle.price || "0.00");
    
    img.src = "/static/images/" + vehicle["_id"] + ".png";

    // Handle tags directly as a string
    tag.textContent = vehicle.tags || "N/A";

    itemView.style.visibility = "visible";
    sidemenu.style.filter = "blur(10px)";
    layout.style.filter = "blur(10px)";
    searchBar.style.filter = "blur(10px)";
    filterview.style.filter = "blur(10px)";
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

function Fetch(){
    console.log("fetching")
    let filters = GetFilters()
    let search = JSON.stringify(filters+searchBar.value)
    fetch("/search",{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(search)
    }).then(response =>{
        if(!response.ok){
            throw new Error("HTTP error! status: "+response.status)
        }
        return response.json()
    }).then(data =>{
        GetVehicles(data)
    }).catch(error => console.log(error))
}

searchBar.addEventListener("input",function(){
    Fetch()
})

let links = document.getElementsByClassName("sidemenu")
for(let i = 0; i < links.length; i++){
    if(links[i].nodeName != "BUTTON") continue;
    links[i].onclick = () => window.location.href = links[i].getAttribute("value")
}
document.getElementById("close").onclick = () => ShowBackground()
var vehicles = JSON.parse(document.currentScript.getAttribute('vehicles'));
//uploadLink.onclick = () => window.location.href = "/upload"
//logout.onclick = () => window.location.href = "/logout"

ShowVehicles(vehicles)

//OLD CODE PUT IN PYTHON
/**
 * 
 * @param {String} name
 * @returns {Array}
 */
/*function GetVehiclesByName(name){
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
}*/

