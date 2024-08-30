var items = [
    {
        "name":"suzuki",
        "category":"bike",
        "description":"some description",
        "price":6000
    },
    {
        "name":"jefferson",
        "category":"bike",
        "description":"i dont know",
        "price":7000
    },
    {
        "name":"third bike",
        "category":"i dont know, im tired",
        "description":"jez, dickhead, do this for me",
        "price":50_000
    }
]
for(let i = 0; i < 12; i++){
    var layout = document.getElementById("layout")
    var newButton = document.createElement("button")
    newButton.className = "item"
    newButton.id = i
    layout.appendChild(newButton)

    var image = document.createElement("img")
    var source = "images/"+i+".png"
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

async function ShowItem(index){
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
    img.src = "images/"+index+".png"
    
    itemView.style.visibility = "visible"
    sidemenu.style.filter = "blur(10px)"
    layout.style.filter = "blur(10px)"
    searchBar.style.filter = "blur(10px)"
}

closeButton.onclick = ShowBackground