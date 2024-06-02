import requests
import json
import pandas as pd

auth = str(input("Enter Authorization: "))

channelid = int(input("Enter The Channel ID you want to export chats from: ")) #Channel ID

limit = int(input("Enter the number of last messages you wanna export: "))  #Number of Last Messages

data = [] 

def retrieve_messages(channelid):
    headers = {
        'authorization': auth
    }
    r= requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit={limit}', headers=headers)
    # Error handeling
    if r.status_code == 200:
        print(r)
        json_loader = json.loads(r.text)
        for value in json_loader:
            print(value)
            liyeko = value['content']
            # print(value['content'], '\n')
            i = 1
            while i < limit:
                i +=1
                data.insert(i, liyeko)
                break
        
        print(data)
        df = pd.DataFrame(data)
        df.to_excel("retrieved_messages.xlsx")
    else:
        print(f"Error: {r.status_code}")
        exit()
    
   
retrieve_messages(channelid)
