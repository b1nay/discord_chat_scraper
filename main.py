import requests
import json
import pandas as pd

auth = str(input("Enter Authorization: "))
if auth == "":
    print("Error: Authorization is required")
    exit()

try:
    channelid = int(input("Enter Channel ID: "))
except ValueError as e:
    print("Error: Channel ID is required")
    exit()

limit = input("Enter the limit of messages you want to export (default: 50): ")
if limit == "":
    limit = 50
else:
    try:
        limit = int(limit)
    except ValueError as e:
        print("Error: Limit must be an integer")
        exit()


data = [] 

def retrieve_messages(channelid):
    headers = {
        'authorization': auth
    }
    r= requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit={limit}', headers=headers)
    # Error handeling
    if r.status_code == 200:
        json_loader = json.loads(r.text)
        for value in json_loader:
            liyeko = value['content']
            i = 1
            while i < limit:
                i +=1
                data.insert(i, liyeko)
                break
        
        df = pd.DataFrame(data)
        df.to_excel("retrieved_messages.xlsx")
    else:
        print(f"Error: {r.status_code}")
        exit()
    print("Messages retrieved successfully")
    
   
retrieve_messages(channelid)