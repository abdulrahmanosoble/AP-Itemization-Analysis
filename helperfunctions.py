import json
import sys
import time
from league import *

class MatchRequest:
    def __init__(self, region, matchId):
        self.region = region
        self.matchId = matchId

    def get(self):
        while True:
            r = requests.get("https://{0}.api.pvp.net/api/lol/{0}/v2.2/match/{1}/?api_key=f2b4dbcc-3a94-4732-9e37-bed4a5f05e63&includeTimeline=true".format(self.region, self.matchId))
        #    if(r.status_code != 429):
        #        print(r.status_code)
            if("Retry-After" not in r.headers):
                time.sleep(1)
                #print("429 - Server Issues")
            else:
                print("429 - WARNING: Rate Limit Exceeded")
                retry = float(r.headers["Retry-After"])
                if not retry: # Header may return retry after 0
                    retry = 1
                print("Retrying after {0}".format(retry))
                time.sleep(retry)
            if(r.status_code==200):
                break
        return r

def getAllMatches(patch):
    queues = ['NORMAL_5X5', 'RANKED_SOLO']
    regions = ['BR', 'EUNE', 'EUW', 'KR', 'LAN', 'LAS', 'NA', 'OCE', 'RU', 'TR']
    matches = []
    for queue in queues:
        for region in regions:
            file = open('AP_ITEM_DATASET/{0}/{1}/{2}.json'.format(patch,queue,region), 'r')
            matchJSON = json.load(file)
            for matchID in matchJSON:
                matchData = MatchRequest(region.lower(), matchID)
                matches.append(matchData)
    return matches

def parseIngredientItems(matchData):
    items = [1026, 1058, 3136]
    ingredients = []
    alreadyBought = []
    for frame in matchData["timeline"]["frames"]:
        if('events' in frame.keys()):
            for event in frame["events"]:
                for key, value in event.items():
                    if(key == "eventType" and value == "ITEM_PURCHASED" and (event["itemId"] in items) and (event["participantId"] not in alreadyBought)):
                        item = event["itemId"]
                        timeBought = event["timestamp"]
                        ingredient = IngredientItem(item,timeBought)
                        ingredients.append(ingredient)
                        alreadyBought.append(event["participantId"])
    return ingredients

def parseMajorItems(matchData):
    items = [3089, 3157, 3285, 3116, 3003, 3040, 3027, 3151, 3115, 3152, 3165, 3174]
    fullItems = [3001,3105,3003,3174,3060,3102,3153,3709,3717,3721,3725,3710,3718,3722,3726,3708,3716,3720,
                 3724,3930,3931,3932,3933,3707,3714,3719,3723,3508,3401,3092,3110,3022,3026,3124,3146,3025,
                 3031,3035,3151,3100,3190,3285,3004,3156,3139,3222,3165,3042,3043,3115,3046,3089,3143,3074,
                 3800,3027,3116,3040,3048,3065,3087,3068,3141,3069,3071,3072,3075,3078,3135,3083,3152,3091,
                 3142,3050,3172,3157,3512]
    majors = []
    winners = []
    orderList = [0,0,0,0,0,0,0,0,0,0,0]
    for team in matchData["teams"]:
        if(team["winner"]):
            winnerId = team["teamId"]
    for participant in matchData["participants"]:
        if(participant["teamId"] == winnerId):
            winners.append(participant["participantId"])
    for frame in matchData["timeline"]["frames"]:
        if('events' in frame.keys()):
            for event in frame["events"]:
                for key, value in event.items():
                    if(key == "eventType" and value == "ITEM_PURCHASED" and event["itemId"] in fullItems):
                        orderList[event["participantId"]] += 1
                    if(key == "eventType" and value == "ITEM_PURCHASED" and (event["itemId"] in items)):
                            item = event["itemId"]
                            timeBought = event["timestamp"]
                            if(event["participantId"] in winners):
                                win = True
                            else:
                                win = False
                            order = orderList[event["participantId"]]
                            majorItem = MajorItem(item,timeBought,order,win)
                            majors.append(majorItem)
    return majors

def parseChampions(matchData):
    items = [3089, 3157, 3285, 3116, 3003, 3040, 3027, 3151, 3153, 3315, 3152, 3165, 3174]
    firstBack = [False,False,False,False,False,False,False,False,False,False]
    participants = []
    for participant in matchData["participants"]:
        participants.append(Champion(participant["championId"]))
    for frame in matchData["timeline"]["frames"]:
        if('events' in frame.keys()):
            for index, event in enumerate(frame["events"]):
                for key, value in event.items():
                    if(key == "eventType" and value == "ITEM_PURCHASED"):
                        p = event["participantId"]
                        if (event["itemId"] in items):
                            participants[p-1].addItem(event["itemId"])
                        if (not firstBack[p-1] and event["timestamp"] > 120000): #Get First back Items
                            firstBack[p-1] = True
                            firstItemTime = event["timestamp"]
                            for ItemBuys in frame["events"]:
                                for key, value in ItemBuys.items():
                                    if(key == "eventType" and value == "ITEM_PURCHASED" and ItemBuys["participantId"] == p):
                                        timeDifference = (ItemBuys["timestamp"] - firstItemTime)
                                        if(timeDifference < 30000):
                                            participants[p-1].addFirstBack(ItemBuys["itemId"])
                                        else:
                                            break
    for p in participants:
        if not p.isMage():
            participants.remove(p)
    return participants
