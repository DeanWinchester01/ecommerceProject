var uploadButton = document.getElementById("imgUpload")
var vehicleImg = document.getElementById("itemImg")
var upload = document.getElementById("Upload")
var returnButton = document.getElementById("Return")



console.log(uploadButton)
uploadButton.onchange = function(){
    let file = uploadButton.files[0]
    let reader = new FileReader()
    reader.onload = function(e){
        vehicleImg.src = e.target.result
    }
    reader.readAsDataURL(file)
    console.log(file)
}

upload.onclick = function(){
    let itemName = document.getElementById("itemName")
    let desc = document.getElementById("desc")
    let price = document.getElementById("price")
    let category = document.getElementById("category")
    console.log(itemName)
    let canUpload = true

    if(itemName.value == ""){
        itemName.value = "Fill in this field"
        canUpload = false
    }

    if(desc.value == ""){
        desc.value = "Fill in this field"
        canUpload = false
    }

    if(price.value == ""){
        price.value = "Fill in this field"
        canUpload = false
    }

    if(category.value == ""){
        category.value = "Fill in this field"
        canUpload = false
    }

    if(!canUpload){
        return
    }
    
    console.log("Upload")
    window.open("page.html","_self")
}

returnButton.onclick = () => window.open("page.html","_self")
