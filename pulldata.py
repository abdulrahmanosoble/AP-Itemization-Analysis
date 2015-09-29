import requests
import json
from io import StringIO
from league import *
from helperfunctions import *
from datetime import *
import time
import threading
from queue import Queue
import os

IngredientItems = []
MajorItems = []
Champions = []
index = 0
patch = 's'

matchQueue = Queue()
matchCount = 0
lock = threading.Lock()
error = 0;
ch = 0

def split(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def processMatches():
    global index
    global patch
    global matchQueue
    global error
    global ch
    while True:
        match = matchQueue.get()
        lock.acquire()
        index += 1
        print("Match {0}: --- Patch {1} --- Chunk {2} --- Processed by {3}".format(index,patch,ch,threading.current_thread()))
        lock.release()
        try:
            data = match.get().json()

            for ingredient in parseIngredientItems(data):
                IngredientItems.append(ingredient)
            for major in parseMajorItems(data):
                MajorItems.append(major)
            for champ in parseChampions(data):
                Champions.append(champ)
            data.clear()
        except:
            error += 1
            print("Error: Match could not be processed")
        matchQueue.task_done()

def getPatchData(patch, name):
    global matchQueue
    global ch
    global index
    del IngredientItems[:]
    del MajorItems[:]
    del Champions[:]
    matches = getAllMatches(patch)
    ch = 0
    for chunk in split(matches,10000):
        index = 0
        ch += 1
        del IngredientItems[:]
        del MajorItems[:]
        del Champions[:]
        for match in chunk:
            matchQueue.put(match)

        matchQueue.join()

        dataJSON = dict({ 'IngredientItems':[], 'MajorItems':[], "Champions":[]  })

        for ingredient in IngredientItems:
            dataJSON["IngredientItems"].append(json.loads(ingredient.to_JSON()))
        for major in MajorItems:
            dataJSON["MajorItems"].append(json.loads(major.to_JSON()))
        for champion in Champions:
            dataJSON["Champions"].append(json.loads(champion.to_JSON()))

        os.makedirs('chunks', exist_ok=True)
        with open('chunks/Patch{0}DataChunk{1}.json'.format(name,ch), 'w') as fp:
            fp.write(json.dumps(dataJSON, indent=4))

        print("Successfully wrote data to chunks/Patch{0}DataChunk{1}.json".format(name,ch))
        print(error)



#Create Threads
for i in range(300):
    t = threading.Thread(target=processMatches, name="Thread {0}".format(i))
    t.daemon = True
    t.start()

patch = "5.11"
getPatchData('5.11', '511')
patch = "5.14"
getPatchData('5.14', '514')
print('{0} files could not be read'.format(error))
