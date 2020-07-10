import csv
import matplotlib.pyplot as plt
import random
walkingAreaXsize = 50
walkingAreaYsize = 50
precision = 98 #  x%
potentialPaths = []
precision = 100-precision
precision = precision*0.01

def plotPath(data, lab):
    x = []
    y = []
    for cordinate in data:
        x.append(cordinate[0])
        y.append(cordinate[1])
    plt.plot(x, y, label=lab)

def predictPattern(data):
    #print(len(data))
    for pattern in paterns:
        #print("trying pattern")
        if len(pattern) >= len(data):            
            #print("pattern in filtering")
            matchedPositions = 0
            for pos in range(len(data)):
                if (data[pos][0] >= pattern[pos][0]) and (data[pos][1] >= pattern[pos][1]):
                    markX = data[pos][0]*precision
                    differenceX = data[pos][0] - pattern[pos][0]
                    markY = data[pos][1]*precision
                    differenceY = data[pos][1] - pattern[pos][1]
                    if (differenceX <= markX) and (differenceY <= markY):
                        matchedPositions+=1
                        print(markX, markY, data[pos], pattern[pos])            
                    else:
                        continue
                        #print("attern failed matching A")
                elif (data[pos][0] <= pattern[pos][0]) and (data[pos][1] <= pattern[pos][1]):
                    markX = pattern[pos][0]*precision
                    differenceX = pattern[pos][0] - data[pos][0]
                    markY = data[pos][1]*precision
                    differenceY = pattern[pos][1] - data[pos][1]
                    if (differenceX <= markX) and (differenceY <= markY):
                        matchedPositions+=1
                        print(markX, markY, data[pos], pattern[pos])        
                    else:
                        #print("pattern failed matching B")
                        continue
                else:
                    continue
                    #print("pattern failed pos diff")
            print(matchedPositions)
            if matchedPositions >= len(data)*precision:
                plotPath(pattern, "matched")
                potentialPaths.append(pattern)
            else:
                continue
        else:
            continue
            #print("pattern too small")




paterns = []
with open('data/testData.csv', newline='') as csvfile:    
    turret = csv.reader(csvfile)
    patternData = list(turret)
    for pattern in patternData:
        for cordIndex in range(len(pattern)): #augment data to use in comparison
            cord = pattern[cordIndex]
            cord = cord.replace("|", ",")
            cord = cord.strip('][').split(', ')
            for pos in range(len(cord)):
                cord[pos] = int(cord[pos])            
            pattern[cordIndex] = cord
        paterns.append(pattern)
        #print(row["PATTERN"].split(", "))        
    #print(paterns, len(paterns))
trip = []

def create_route_to_match(tripLength):
    for routeIndex in range(random.randint(5, tripLength)):    
        if trip == []:
            x = random.randint(0, walkingAreaXsize)
            y = random.randint(0, walkingAreaYsize)
            trip.append([x, y])
        else:
            x = trip[routeIndex-1]
            x = random.randint(x[0]-1,x[0]+1)
            y = trip[routeIndex-1]
            y = random.randint(y[1]-1,y[1]+1)
            trip.append([x, y])

create_route_to_match(10)
predictPattern(trip)
    
plotPath(trip, "TO MATCH")
plt.legend()
print(potentialPaths)
plt.show()
