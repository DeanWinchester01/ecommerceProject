from flask import Flask, Blueprint, jsonify, request
searchBp = Blueprint("Search", __name__)

vehicles = []

def GetVehiclesByName(name: str, vehicles: list):
    allCurrentVehicles = vehicles
    name = name[1:-1]
    print(name)
    if name == "":
        return allCurrentVehicles
    
    newList = []

    for i in range(len(allCurrentVehicles)):
        vehicle: dict = allCurrentVehicles[i]
        vehicleName: str = vehicle.get("vehicle") or vehicle.get("name")

        if name in vehicleName.lower():
            newList.append(vehicle)

    print("returned new list")
    return newList

def GetVehiclesByTag(vehicles: list, tags: list):
    allCurrentVehicles = vehicles
    if len(tags) == 0:
        return allCurrentVehicles
    
    newList = []
    for vehicle in range(len(vehicles)-1, 0, -1):
        if vehicles[vehicle].get("tags") == None:
            vehicles.pop(vehicle)

    #print(tags)
    for vehicle in range(len(vehicles)-1, 0, -1):
        currentVehicle: dict = vehicles[vehicle]

        #print(currentVehicle.get("tags"))
        #print(currentVehicle)
        if currentVehicle.get("tags") == None or len(currentVehicle.get("tags")) < 1: continue
        #print("searching for tags")
        for tag in range(len(tags)):
            currentTag:str = tags[tag]
            currentTag = currentTag[1:-1]

            #print(type(tags[tag]))
            #print(currentTag)
            #print("searching tag: ",tags[tag])
            #print(currentVehicle.get("tags"))
            if not currentTag in currentVehicle.get("tags"):
                allCurrentVehicles.pop(vehicle)
                #print("vehicle with tags ",currentVehicle.get("tags")," does not include ",currentTag)
            else:
                newList.append(currentVehicle)
                #print("vehicle ",vehicle," includes ",currentTag)
                break

    return newList
    
def SearchForVehicles(search: str, allVehicles: list):
    searchParameters = search.split(" ")
    vehicleName = ""
    tags = []

    for i in range(len(searchParameters)):
        param = searchParameters[i].lower()
        if param[1] == "#" and  len(param) > 3:
            tags.append(param)

        if not "#" in param and vehicleName == "":
            vehicleName = param.lower()

    
    vehicleList = GetVehiclesByName(vehicleName, allVehicles)
    #print(vehicleList)
    newList = GetVehiclesByTag(vehicleList, tags)
    #print(newList)
    return newList

@searchBp.route("/search", methods = ["POST"])
def Search():
    data = request.get_json()
    search = SearchForVehicles(data, vehicles)
    vehicleList = []

    for vehicle in range(len(search)):
        vehicleList.append(search[vehicle]["_id"])

    return jsonify(vehicleList)