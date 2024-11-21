var headerTitle = document.getElementById("header-title")
var itemView = document.getElementById("itemview")
var rightHeader = document.getElementById("header-right")
var layout = document.getElementById("layout")
var searchBar = document.getElementById("searchbar")
var filterview = document.getElementById("filterview")

var itemName = document.getElementById("name")
var category = document.getElementById("category")
var desc = document.getElementById("description")
var price = document.getElementById("price")
var tags = document.getElementById("tags")
var privatePage = false

let parts = document.cookie.split("; ")
let data = {}
for(let i = 0; i < parts.length; i++){
    let key = parts[i].split("=")[0]
    let val = parts[i].split("=")[1]
    data[key] = val
}
document.getElementById("welcome").textContent = data["username"]

function ShowBackground(){
    itemView.style.visibility = "hidden"
    headerTitle.style.filter = "none"
    rightHeader.style.filter = "none"
    layout.style.filter = "none"
    searchBar.style.filter = "none"

    if(!privatePage)
        filterview.style.filter = "none"
}

/**
 * @param {Array} vehicleList 
 */
function ShowVehicles(vehicleList) {
    vehicleList.forEach(function(vehicle) {
        let div = document.createElement("div");
        div.className = "item-container";
        div.id = vehicle["_id"];

        let button = document.createElement("button");
        button.id = vehicle["_id"];
        button.className = "item";

        if(window.location.href.length > 26) {
            privatePage = true
            let del = document.createElement("button");
            del.className = "delete";
            div.append(del);

            // Create and append the span for the delete icon
            let iconSpan = document.createElement("span");
            iconSpan.className = "material-symbols-outlined";
            iconSpan.textContent = "delete"; // Material icon text
            del.append(iconSpan);

            // Create and append the paragraph for the text "Delete"
            let deleteText = document.createElement("p");
            deleteText.textContent = "Delete";
            del.append(deleteText);

            del.onclick = function() {
                window.location.href = "/delete/" + vehicle["_id"];
            };
        }

        let image = document.createElement("img");
        image.className = "itemImage";
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
        layout.appendChild(div);

        button.onclick = function() {
            ShowItem(vehicle);
        };
    });
}

function ShowItem(vehicle) {
    let updateForm = document.getElementById("form")
    if(updateForm != null)
        updateForm.action = "/update/"+vehicle["_id"]

    let name = document.getElementById("name-custom") || document.getElementById("name");
    let cat = document.getElementById("category-custom") || document.getElementById("category");
    let description = document.getElementById("description-custom") || document.getElementById("description");
    let pr = document.getElementById("price-custom") || document.getElementById("price");
    let img = document.getElementById("itemImage");
    let tag = document.getElementById("tags-custom") || document.getElementById("tags");

    if(name.localName == "span"){
        name.textContent = vehicle.name
        cat.textContent = vehicle.category || "Uncategorized";
        description.textContent = vehicle.description || "No description available";
        pr.textContent = "$"+vehicle.price
        tag.textContent = vehicle.tags;
    }
    else{
        name.value = vehicle.name;
        cat.value = vehicle.category || "Uncategorized";
        description.value = vehicle.description || "No description available";
        pr.value = vehicle.price
        tag.value = vehicle.tags;
    }
    
    img.src = "/static/images/" + vehicle["_id"] + ".png";

    itemView.style.visibility = "visible";
    headerTitle.style.filter = "blur(10px)";
    rightHeader.style.filter = "blur(10px)";
    layout.style.filter = "blur(10px)";
    searchBar.style.filter = "blur(10px)";
    
    if(!privatePage)
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
    console.log(filters)
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

ShowVehicles(vehicles)
document.currentScript.setAttribute("vehicles","")

