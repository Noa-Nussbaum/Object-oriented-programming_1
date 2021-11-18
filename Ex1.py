import csv
import building
import calls

# Let's create a new calls object
CAddress = 'Calls_d.csv'
c = calls.calls(CAddress)
# Let's create a new building object
BAddress = 'B5.json'
b = building.building(BAddress)

elevStops = []
for i in range(b.numE):
    elevStops.append([])

def dist(curr, j, src):#time until elevator number e gets to floor
    stops = 0
    if len(elevStops[j]) != 0:
        stops = len(elevStops[j])
    elev = building.elevator(b.elevators[j])
    gap = abs(int(curr)-int(src))
    answer = (elev.close + elev.start + elev.stop + elev.open) * stops
    answer = answer + gap/elev.speed
    return answer




#list holds the current locations of all elevators
def allocateTo(call):
        for i in range(0, len(c.calls)): #for every call
            if (b.numE == 1):  # if only one elevator
                c.calls[i][5] = 0 #all calls get elevator 0
            else:
                src = c.calls[i][2] #get src
                dest = c.calls[i][3] #get dest
                temp = 0
                for j in range(b.numE):
                    if(src<dest): #call going up
                        if(int(b.list[j])<=int(src)):
                            if(dist(b.list[j],j,int(src))<dist(b.list[temp],temp,int(src))):
                                temp =j
                        else:
                            temp = (i)%b.numE
                    else:  # call going down
                        if(int(b.list[j])>=int(src)):
                            if(dist(b.list[j],j, int(src)) < dist(b.list[temp],temp, int(src))):
                                temp = j
                        else:
                            temp = (i*j) % b.numE
                    elevStops[temp].append(src)
                    elevStops[temp].append(dest)
                    b.list[temp] = dest
                    c.calls[i][5] = temp




allocateTo(c.calls)

# Let's upload the csv file
with open('out.csv', 'w', newline="") as file:
    write = csv.writer(file)
    write.writerows(c.calls)
