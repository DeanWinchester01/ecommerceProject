
for(var i = 0; i < 12; i++){
    var layout = document.getElementById("layout")
    var newButton = document.createElement("button")
    newButton.className = "item"
    layout.appendChild(newButton)

    var image = document.createElement("img")
    var source = i+".png"
    console.log(source)
    image.src = source
    newButton.appendChild(image)

    image.className = "itemImage"
}