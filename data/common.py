import json

def loadJson(path):
    jsonFile = open(path, "r")
    data = json.load(jsonFile)
    jsonFile.close()
    return data