from flask import Flask, Blueprint, jsonify, request
searchBp = Blueprint("Search", __name__)

vehicles = []

def GetVehiclesByName(name: str, vehiclesList: list):
    allCurrentVehicles = vehiclesList
    
    if name == "":
        return allCurrentVehicles
    
    newList = []

    for i in range(len(allCurrentVehicles)):
        vehicle: dict = allCurrentVehicles[i]
        vehicleName: str = vehicle.get("vehicle") or vehicle.get("name")

        if name in vehicleName.lower():
            newList.append(vehicle)


    return newList

def GetVehiclesByTag(vehiclesList: list, tags: list):
    allCurrentVehicles = []
    for x in vehiclesList:
        allCurrentVehicles.append(x)#append items instead of copying list to prevent items from being removed
        
    if len(tags) == 0:
        return allCurrentVehicles
    
    newList = []
    print(len(allCurrentVehicles))
    for vehicle in range(len(allCurrentVehicles)-1, 0, -1):
        if allCurrentVehicles[vehicle].get("tags") == None:
            allCurrentVehicles.pop(vehicle)

    for vehicle in range(len(allCurrentVehicles)-1, 0, -1):
        currentVehicle: dict = allCurrentVehicles[vehicle]

        if currentVehicle.get("tags") == None or len(currentVehicle.get("tags")) < 1: continue
        for tag in range(len(tags)):
            currentTag:str = tags[tag]
            
            if not currentTag in currentVehicle.get("tags"):
                allCurrentVehicles.pop(vehicle)
            else:
                newList.append(currentVehicle)
                break

    return newList

def GetVehicleByPrice(vehicleList: list, lower: int, higher: int):
    allCurrentVehicles = []
    for x in vehicleList:
        allCurrentVehicles.append(x)
    print(allCurrentVehicles)

    print(type(lower), lower, type(higher), higher)
    if lower == 0 and higher == 0:
        print("returning all vehicles")
        return vehicleList
    
    print("generating new list")
    newList = []
    print(len(allCurrentVehicles))
    for vehicle in range(len(allCurrentVehicles)):
        print(vehicle)
        currentVehicle: dict = allCurrentVehicles[vehicle]
        vehiclePrice = int(currentVehicle["price"])
        print("vehicle: ",currentVehicle)
        print(type(vehiclePrice),vehiclePrice)

        if vehiclePrice > lower and vehiclePrice < higher:
            newList.append(currentVehicle)

    print(newList)
    return newList

    
def SearchForVehicles(search: str, allVehicles: list):
    searchParameters = search.split(" ")
    print(searchParameters)
    vehicleName = ""
    tags = []
    lower, higher = 0,0

    for i in range(len(searchParameters)):
        param = searchParameters[i].lower()
        
        if len(param) == 0:#empty parameter
            continue
        
        if param[0] == "#" and  len(param) > 1:
            tags.append(param)

        if "-" in param:
            nums = param.split("-")
            print("nums",nums)
            lower = int(nums[0])
            print("lower", lower)
            higher = int(nums[1])
            print("higher", higher)

        if not "#" in param and not "-" in param and vehicleName == "":
            vehicleName = param.lower()

    vehicleList = GetVehiclesByName(vehicleName, allVehicles)
    newList = GetVehiclesByTag(vehicleList, tags)
    newList = GetVehicleByPrice(newList, lower, higher)
    return newList

@searchBp.route("/search", methods = ["POST"])
def Search():
    data = request.get_json()
    #print(data)
    data = data[1:-1]
    search = SearchForVehicles(data, vehicles)
    vehicleList = []

    for vehicle in range(len(search)):
        vehicleList.append(search[vehicle]["_id"])

    return jsonify(vehicleList)