import requests
import json

class IngredientItem():
    def __init__(self, itemId, timeBought):
        self.itemId = itemId
        self.timeBought = timeBought

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class MajorItem:
    def __init__(self, itemId, timeBought, order, win):
        self.itemId = itemId
        self.timeBought = timeBought
        self.order = order
        self.win = win

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Champion:
    def __init__(self, championId):
        self.championId = championId
        self.items = []
        self.firstBack = []

    def addItem(self, item):
        self.items.append(item)

    def addFirstBack(self, item):
        consumables = [2003, 2004, 2009, 2010, 2044, 2043, 3340, 3361, 3362, 3364, 3342, 3341]
        if item not in consumables:
            self.firstBack.append(item)

    def isMage(self):
        mages = [103,84,32,34,1,268,63,69,31,131,60,28,81,9,105,245,3,41,74,30,38,55,10,85,96,7,127,117,99,90,25,76,61,68,13,27,50,134,17,4,161,112,8,101,115,143,26]
        if self.championId in mages:
            return True
        else:
            return False

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
