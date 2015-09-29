import json
import io
from operator import itemgetter
import datetime
import requests


def processPatch(patch):
    data = { "Items": [{ 1026: {"sumTime": 0 }}, {1058: {"sumTime": 0 }}, {3136: {"sumTime": 0}},
            {3089: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3157: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3285: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3116: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3003: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3027: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3151: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3115: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3152: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3165: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            },
            {3174: {
                "sumTime": 0,
                "order": -1,
                "winRate": -1 }
            }
        ],
        "Champions": [
            {103:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {84:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {32:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {34:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {1:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {268:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {63:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {69:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {31:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {131:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {60:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {28:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {81:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {9:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {105:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {245:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {3:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {41:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {74:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {30:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {38:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {55:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {10:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {85:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {96:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {7:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {127:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {117:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {99:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {90:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {25:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {76:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {61:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {68:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {13:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {27:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {50:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {134:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {17:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {4:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {161:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {112:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {8:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {101:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {115:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {143:{
                "mostCommonItems": [],
                "firstBack": []}
            },
            {26:{
                "mostCommonItems": [],
                "firstBack": []}
            }
        ] }

    intermediate = { "Items": [{1026: {"sumTime": 0, "total": 0}}, {1058: {"sumTime": 0, "total": 0}}, {3136: {"sumTime": 0, "total": 0}},
            {3089: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3157: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3285: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3116: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3003: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3027: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3151: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3115: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3152: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }},{
            3165: {
                "sumTime": 0,
                "order": [],
                "win": 0,
                "total": 0
            }},{
            3174: {
                "sumTime": 0,
                "order": [] ,
                "win": 0,
                "total": 0
            }}
        ],
        "Champions": [
            {103:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {84:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {32:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {34:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {1:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {268:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {63:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {69:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {31:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {131:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {60:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {28:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {81:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {9:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {105:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {245:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {3:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {41:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {74:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {30:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {38:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {55:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {10:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {85:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {96:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {7:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {127:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {117:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {99:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {90:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {25:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {76:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {61:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {68:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {13:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {27:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {50:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {134:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {17:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {4:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {161:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {112:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {8:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {101:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {115:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {143:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            },
            {26:{
                "mostCommonItems": [],
                "firstBack": [], "total": 0}
            }
        ] }
    for i in range(20):
        f = open("chunks/Patch{0}DataChunk{1}.json".format(patch,i+1), 'r')
        rawdata = json.load(f)
        for ingredient in rawdata["IngredientItems"]:
            for item in intermediate["Items"]:
                if (ingredient["itemId"] in item.keys()):
                    item[ingredient["itemId"]]["sumTime"] += ingredient["timeBought"]
                    item[ingredient["itemId"]]["total"] += 1

        for major in rawdata["MajorItems"]:
            for item in intermediate["Items"]:
                if (major["itemId"] in item.keys()):
                    item[major["itemId"]]["sumTime"] += major["timeBought"]
                    orderFlag = True
                    for o in item[major["itemId"]]["order"]:
                        if(o[0] == major["order"]):
                            o[1] += 1
                            orderFlag = False
                    if orderFlag:
                        item[major["itemId"]]["order"].append([major["order"],1])
                    if major["win"]:
                        item[major["itemId"]]["win"] += 1
                    item[major["itemId"]]["total"] += 1

        for champion in rawdata["Champions"]:
            for champ in intermediate["Champions"]:
                if (champion["championId"] in champ.keys()):
                    cid = champion["championId"]
                    champ[cid]["total"] += 1
                    for item in champion["items"]:
                        itemFlag = True
                        for entry in champ[cid]["mostCommonItems"]:
                            if (entry[0] == item):
                                entry[1] += 1
                                itemFlag = False
                        if itemFlag:
                            champ[cid]["mostCommonItems"].append([item,1])
                    fb = champion["firstBack"]
                    fbFlag = True
                    for entry in champ[cid]["firstBack"]:
                        if (sorted(entry[0]) == sorted(fb)):
                            entry[1] += 1
                            fbFlag = False
                    if fbFlag:
                        champ[cid]["firstBack"].append([sorted(fb),1])
        print("Finished Processing Patch {0} Chunk {1}".format(patch,i+1))

    #sort intermediate data and add image

    for item in intermediate["Items"]:
        for value in item.values():
            if "order" in value:
                value["order"] = sorted(value["order"], key=itemgetter(1), reverse=True)

    for champ in intermediate["Champions"]:
        for value in champ.values():
            value["mostCommonItems"] = sorted(value["mostCommonItems"], key=itemgetter(1), reverse=True)
            value["firstBack"] = sorted(value["firstBack"], key=itemgetter(1), reverse=True)

    #Turn intermediate data into final data

    for idx, item in enumerate(data["Items"]):
        for itemId, itemData in item.items():
            int = intermediate["Items"][idx][itemId]
            if int["total"]:
                sumTime = (int["sumTime"] / int["total"]) / 1000
                m, s = divmod(sumTime,60)
                m = round(m)
                s = round(s)
                if (s == 60):
                    s = 0
                    m += 1
                t = datetime.time(0,m,s,0)
                itemData["sumTime"] = "{:%M:%S}".format(t)
                if("win" in int.keys()):
                    winRate = int["win"] / int["total"]
                    itemData["winRate"] = "{:.2%}".format(winRate)
            if ("order" in int.keys()):
                itemData["order"] = int["order"][0][0]
            r = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item/{0}/?api_key=f2b4dbcc-3a94-4732-9e37-bed4a5f05e63&itemData=image".format(itemId))
            itemData["imageurl"] = "http://ddragon.leagueoflegends.com/cdn/5.16.1/img/item/{0}".format(r.json()["image"]["full"])


    for idx, champ in enumerate(data["Champions"]):
        for champId, champData in champ.items():
            int = intermediate["Champions"][idx][champId]
            champData["firstBack"] = int["firstBack"][0:10]
            champData["mostCommonItems"] = int["mostCommonItems"][0:10]
            fbSum = sum(col[1] for col in champData["firstBack"])
            for fb in champData["firstBack"]:
                fb[1] = "{0:.2%}".format(fb[1] / fbSum)
            itemsSum = sum(col[1] for col in champData["mostCommonItems"])
            for item in champData["mostCommonItems"]:
                item[1] = "{0:.2%}".format(item[1] / itemsSum)
            r = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/champion/{0}/?api_key=f2b4dbcc-3a94-4732-9e37-bed4a5f05e63&champData=image".format(champId))
            champData["imageurl"] = "http://ddragon.leagueoflegends.com/cdn/5.16.1/img/item/{0}".format(r.json()["image"]["full"])
            data["Images"] = {}
            for items in champData["firstBack"]:
                for item in items[0]:
                    if item not in data["Images"].keys():
                        r = requests.get("https://global.api.pvp.net/api/lol/static-data/euw/v1.2/item/{0}/?api_key=f2b4dbcc-3a94-4732-9e37-bed4a5f05e63&itemData=image".format(item))
                        data["Images"][item] = "http://ddragon.leagueoflegends.com/cdn/5.16.1/img/item/{0}".format(r.json()["image"]["full"])

    os.makedirs('final', exist_ok=True)
    with open('final/Patch{0}AggregateData.json'.format(patch), 'w') as fp:
        fp.write(json.dumps(data, indent=4))


processPatch('511')
processPatch('514')
