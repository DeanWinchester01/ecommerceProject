/*console.log("fetching user data");
//let cookies = document.cookie.split(";");
let target;
console.log(window.location.pathname.length > 5)
if(window.location.pathname.length > 5){
    let email = cookies[0].split("=")[1]
    target = email
}else{
    target = "public"
}
    
fetch("/page/getdata/"+target)
.then(response =>{
    if(!response.ok){
        throw new Error("HTTP error! status: "+response.status)
    }
    return response.json()
}).then(data =>{
    vehicles = data
    ShowVehicles(vehicles)
}).catch(error => console.log(error))*/
// Retrieve and parse the JSON data from the "vehicles" attribute
/*const vehicleData = JSON.parse(document.currentScript.getAttribute('vehicles'));
vehicles = vehicleData
ShowVehicles(vehicleData)
console.log(vehicleData); // Should log the vehicle data array

*/