var items = [
    {
        "name":"Yamaha YZF-R7 R7 HO 2023",
        "category":"Motorbike",
        "description":"N/A",
        "price":16_099
    },
    {
        "name":"Yamaha YZF-R3 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":9_675
    },
    {
        "name":"Yamaha YZ450FX",
        "category":"Motorbike",
        "description":"N/A",
        "price":16_249
    },
    {
        "name":"Yamaha XSR900 GP 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":22_799
    },
    {
        "name":"Yamaha Tenere 700 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":20_180
    },
    {
        "name":"Yamaha AG125 2023",
        "category":"Motorbike",
        "description":"N/A",
        "price":5_299
    },
    {
        "name":"Yamaha MT-07 2023",
        "category":"Motorbike",
        "description":"N/A",
        "price":14_099
    },
    {
        "name":"Kawasaki ZX6R Ninja 636 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":21_495
    },
    {
        "name":"Kawasaki Z1000 ABS 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":19_916
    },
    {
        "name":"Kawasaki KX85 Big Wheel 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":8_495
    },
    {
        "name":"Kawasaki KLE300 Versys-X 300 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":9_060
    },
    {
        "name":"Kawasaki EX500 Ninja 500 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":8_995
    },
    {
        "name":"Kawasaki EN650 Vulcan SE 2024",
        "category":"Motorbike",
        "description":"N/A",
        "price":12_866
    },
    {
        "name":"2017 Honda Civic",
        "category":"Car",
        "description":"N/A",
        "price":16_950
    },
    {
        "name":"2019 Jaguar F-Type",
        "category":"Car",
        "description":"N/A",
        "price":139_990
    },
    {
        "name":"2022 Toyota Corolla",
        "category":"Car",
        "description":"N/A",
        "price":31_980
    },
    {
        "name":"2022 Tesla Model Y",
        "category":"Car",
        "description":"N/A",
        "price":49_990
    },
    {
        "name":"2024 Kia Sportage",
        "category":"Car",
        "description":"N/A",
        "price":39_990
    },
    {
        "name":"2024 Volkswagen ID.4",
        "category":"Car",
        "description":"N/A",
        "price":53_990
    },
    {
        "name":"2022 Hyundai Kona",
        "category":"Car",
        "description":"N/A",
        "price":33_990
    },
    {
        "name":"2015 Nissan GTR",
        "category":"Car",
        "description":"N/A",
        "price":139_990
    },
    {
        "name":"2019 Chevrolet Camaro",
        "category":"Car",
        "description":"N/A",
        "price":109_990
    },
    {
        "name":"2024 Audi Q7",
        "category":"Car",
        "description":"N/A",
        "price":167_990
    }

]
for(let i = 0; i < 12; i++){
    var layout = document.getElementById("layout")
    var newButton = document.createElement("button")
    newButton.className = "item"
    newButton.id = i
    layout.appendChild(newButton)

    var image = document.createElement("img")
    var source = "images/" + i+".png"
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
    itemView.style.visibility = "visible"
    img.src = "images/" + index+".png"
}

closeButton.onclick = ShowBackground
//document.getElementById("0").onclick = function(){
    //ShowItem("0")
//}