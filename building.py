import json

import numpy as np


class building:
    # Let's upload the JSON file
    def __init__(self, file_name):
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
                self.minFloor = data["_minFloor"]
                self.maxFloor = data["_maxFloor"]
                self.numF = (self.maxFloor - self.minFloor)
                ele = []
                for el in data["_elevators"]:
                    # elev = ele[el]
                    ele.append(el)
                self.elevators = ele.copy()
                self.numE = len(self.elevators)
                list =[]
                self.list = [0 for i in range(0,self.numE)]

        except IOError as e:
            print(e)


class elevator:

    def __init__(self,dict):
        self.id = dict["_id"]
        self.speed = dict["_speed"]
        self.close = dict["_closeTime"]
        self.open = dict["_openTime"]
        self.start = dict["_startTime"]
        self.stop = dict["_stopTime"]




