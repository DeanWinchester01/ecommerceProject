var layout = document.getElementById("layout")
if (document.cookie.includes("email")){
    
    let parts = document.cookie.split("; ")
    let data = {}
    for(let i = 0; i < parts.length; i++){
        let key = parts[i].split("=")[0]
        let val = parts[i].split("=")[1]
        data[key] = val
    }
    
    let userLink = document.getElementById("uploads")
    userLink.value += data["username"]
    
    if (data["loggedIn"] == "True")
        document.getElementById("welcome").textContent = data["username"]
}

var options = document.getElementsByClassName("sideoption")
function GetFilters(){
    let filters = ""
    for(let i = 0; i < options.length; i++){
        let selector = options[i].querySelector(".selector")
        let data = options[i].querySelector(".data")
        
        if(selector.checked){
            console.log(data.getAttribute("value"))
            filters += data.getAttribute("value") + " "

        }
    }
    
    return filters
}

for(let i = 0; i < options.length; i++){
    let child = options[i].querySelector(".selector")
    child.onclick = Fetch
        
}