import requests
import json

def main():
    rawFile = open("MWIdata.json", "w+")
    rawFile.write(((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text))
    filteredFile = open("HouseRooms.txt", "w+")
    
    filteredFile.write(filterRooms((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text))
    
def filterRooms(text):
    new = text[2631373:2696862]
    new = new.replace("sortIndex", "\n\n")
    new = new.replace(",", " ")
    new = new.replace("\"","")
    new = new.replace("/", "")
    new = new.replace("items", "")
    new = new.replace("itemHrid", "")
    new = new.replace(":", "")
    new = new.replace("[", "")
    new = new.replace("]", "")
    new = new.replace("}", "")
    new = new.replace("{", "")
    for char in "123456789":
        new = new.replace(char+"coin","\nRoom Level "+char+":\tcoin")
    new = new.replace(" count", "-")
    #roomList = new.split("\n\n")
    #print(roomList)
    #new = "Archery Range" + new[706:]
    return new


if __name__ == "__main__":
    main()