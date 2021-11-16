import csv
import json
import numpy as np
import building
import calls
import pandas as pd



# Let's create a new calls object
CAddress = '/Users/nnussbaum/Ariel/Year 2 - 1/עבודות להגשה/Ex1_input/Ex1_Calls/Calls_d.csv'
c = calls.calls(CAddress)
# Let's create a new building object
BAddress = '/Users/nnussbaum/Ariel/Year 2 - 1/עבודות להגשה/Ex1_input/Ex1_Buildings/B5.json'
b = building.building(BAddress)


def dist(curr,e,src):#time until elevator number e gets to floor
    elev = building.elevator(b.elevators[e])
    gap = abs(int(curr)-int(src))
    answer = elev.close + elev.start + gap/elev.speed + elev.stop + elev.open
    return answer




#list holds the current locations of all elevators
def allocateTo(call):
    if(b.numE==1): #if only one elevator
        #e = building.elevator(b.elevators[0])
        a = c.calls[c.calls[:, 2].argsort()] #sort calls by source
        for i in range(0, len(c.calls)): #for every call
            c.calls[i][5] = 0 #all calls get elevator 0
            src = c.calls[i][2] #get src
            dest = c.calls[i][3] #get dest
            b.list[0]=dest
            # e.floors.append(src) #add source
            # e.curr = dest
            #e.floors.append(dest) #add dest
        # e.floors.sort() #sort calls by order

    #what would happen if we only looked at the up/down calls
    #the part that takes care of one elevator instance is inaccurate.
    # need to change so that it takes care of direction

    else: #if more than one elevator
        for i in range(0, len(c.calls)):
            src = c.calls[i][2]  # get src
            dest = c.calls[i][3]  # get dest
            temp = 0
            for j in range(0, b.numE):
                if(src<dest): #call going up
                    if(int(b.list[j])<=int(src)):
                        if(dist(b.list[j],j,int(src))<dist(b.list[temp],temp,int(src))):
                            temp =j
                    b.list[temp]=dest
                    c.calls[i][5]=temp #can i move this to end so to not repeat?
                if(src>dest):  # call going down
                    if(int(b.list[j])>=int(src)):
                        if(dist(b.list[j],j, int(src)) < dist(b.list[temp],temp, int(src))):
                            temp = j
                    b.list[temp] = dest
                    c.calls[i][5] = temp  # can i move this to end so to not repeat?


allocateTo(c.calls)

# Let's upload the csv file
with open('out.csv', 'w', newline="") as file:
    write = csv.writer(file)
    write.writerows(c.calls)
