import requests
import json

def main():
    file = open("MWIdata.json", "w+")
    file.write(((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text))
    #print(file.read())
    #full = (((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text)[2631373:2696862]).replace(",", " ").replace("\"","")
    #print(full.find("{\"/house_rooms/archery_range\""))
    #print(full.find("\"count\":2000}]},\"sortIndex\":5}}"))
    #full = full[full.find("{\"/house_rooms/archery_range\""):full.find("\"count\":2000}]},\"sortIndex\":5}}")]
    #full = full[2631373:2696862]
    full = takeOut((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text)
    print(full)
    
def takeOut(text):
    new = text[2631373:2696862]
    for char in new:
        new = new.replace("sortIndex\":15", "\n")
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
    return new


if __name__ == "__main__":
    main()