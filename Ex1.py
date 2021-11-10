import csv
import json
import numpy as np
import elevator
import pandas as pd


BAddress = open('/Users/nnussbaum/Ariel/Year 2 - 1/עבודות להגשה/Ex1_input/Ex1_Buildings/B1.json')
CAddress = open('/Users/nnussbaum/Ariel/Year 2 - 1/עבודות להגשה/Ex1_input/Ex1_Calls/Calls_a.csv')

# Let's upload the JSON file
with BAddress as f:
  data = json.load(f)s
building = json.dumps(data)
BAddress.close
data = json.loads(building)


# Let's upload the csv file
csvreader = csv.reader(CAddress)
rows=[]
for row in csvreader:
  rows.append(row)
CAddress.close

#This is the calls array
calls = np.array(rows)

#Let's get all the building's info:
min = data['_minFloor']
max = data['_maxFloor']
numF= max-min
list =[]
list = data['_elevators']
numE = len(list)

#Let's put all of the elevators into an array
elist= [len(list)]
for i in list:
  elist[i]=list[i]


