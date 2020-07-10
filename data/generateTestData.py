import csv
import random
import matplotlib.pyplot as plt
tripMax = 30
testData = []
walkingAreaXsize = 40
walkingAreaYsize = 40
population = 10000

for person in range(population):
    trip = []
    for routeIndex in range(random.randint(0, tripMax)):    
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
    testData.append(trip)

with open('testData.csv', 'w', newline='') as csvfile:
    fieldnames = ['pattern']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer= csv.writer(csvfile)
    for testarray in testData:
        plt.plot(testarray)
        for cord in testarray:
            cord = str(cord).replace(",", "|")
            print(cord)
        writer.writerow(testarray)

plt.show()