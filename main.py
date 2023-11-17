import requests
import json

def main():
    rawFile = open("MWIdata.json", "w+")
    rawFile.write(((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text))
    filteredFile = open("HouseRooms.txt", "w+")
    #print(file.read())
    #full = (((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text)[2631373:2696862]).replace(",", " ").replace("\"","")
    #print(full.find("{\"/house_rooms/archery_range\""))
    #print(full.find("\"count\":2000}]},\"sortIndex\":5}}"))
    #full = full[full.find("{\"/house_rooms/archery_range\""):full.find("\"count\":2000}]},\"sortIndex\":5}}")]
    #full = full[2631373:2696862]
    full = takeOut((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text)
    filteredFile.write(full)
    
def takeOut(text):
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