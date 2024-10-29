from flask import Flask, Blueprint, jsonify, request
searchBp = Blueprint("Search", __name__)

vehicles = []

def GetVehiclesByName(name: str, vehiclesList: list):
    allCurrentVehicles = vehiclesList
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

def GetVehiclesByTag(vehiclesList: list, tags: list):
    allCurrentVehicles = []
    for x in vehiclesList:
        allCurrentVehicles.append(x)#append items instead of copying list to prevent items from being removed
        
    if len(tags) == 0:
        return allCurrentVehicles
    
    newList = []
    for vehicle in range(len(allCurrentVehicles)-1, 0, -1):
        if allCurrentVehicles[vehicle].get("tags") == None:
            allCurrentVehicles.pop(vehicle)

    for vehicle in range(len(allCurrentVehicles)-1, 0, -1):
        currentVehicle: dict = allCurrentVehicles[vehicle]

        if currentVehicle.get("tags") == None or len(currentVehicle.get("tags")) < 1: continue
        for tag in range(len(tags)):
            currentTag:str = tags[tag]
            currentTag = currentTag[1:-1]
            
            if not currentTag in currentVehicle.get("tags"):
                allCurrentVehicles.pop(vehicle)
            else:
                newList.append(currentVehicle)
                break

    return newList
    
def SearchForVehicles(search: str, allVehicles: list):
    searchParameters = search.split(" ")
    vehicleName = ""
    tags = []

    for i in range(len(searchParameters)):
        param = searchParameters[i].lower()
        print(param)
        if param[1] == "#" and  len(param) > 3:
            tags.append(param)

        if not "#" in param and vehicleName == "":
            vehicleName = param.lower()

    vehicleList = GetVehiclesByName(vehicleName, allVehicles)
    newList = GetVehiclesByTag(vehicleList, tags)
    return newList

@searchBp.route("/search", methods = ["POST"])
def Search():
    data = request.get_json()
    data = data[1:-1]
    search = SearchForVehicles(data, vehicles)
    vehicleList = []

    for vehicle in range(len(search)):
        vehicleList.append(search[vehicle]["_id"])

    return jsonify(vehicleList)