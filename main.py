import requests
import json

def main():
    file = open("MWIdata.json", "w+")
    file.write((requests.get('https://raw.githubusercontent.com/silent1b/MWIData/main/init_client_info.json')).text)
    #response.json()
    #html_data = response.text
    

if __name__ == "__main__":
    main()