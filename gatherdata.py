import requests
import json
from io import StringIO
from league import *


f = open('AP_ITEM_DATASET/5.11/RANKED_SOLO/EUW.json', 'r')
matchID = json.load(f)
f.close()

match = requests.get("https://euw.api.pvp.net/api/lol/euw/v2.2/match/{0:d}?api_key=f2b4dbcc-3a94-4732-9e37-bed4a5f05e63&includeTimeline=true".format(matchID[0]))
matchData = match.json()
f = open('patch511Data.json', 'r+')
patchData = json.load(f)

# Connect participants IDs to champion IDs
participants = [-1]
for participant in matchData["participants"]:
    participants.append(participant["championId"])

#Ingredient Item Data gotten by iterating through events

for frame in matchData["timeline"]["frames"][1:]:
    for event in frame["events"]:
        for key, value in event.items():
            if(key == "eventType" and value == "ITEM_PURCHASED" and (event["itemId"] == 1026 or event["itemId"] == 1058)):
                item = event["itemId"]
                time = event["timestamp"]
                ingredient = IngredientItem(item,time)
