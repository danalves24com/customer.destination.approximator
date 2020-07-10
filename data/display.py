import csv
import matplotlib.pyplot as plt
def predictPattern(data):
    print(data)

def plotPath(data):
    x = []
    y = []
    for cordinate in data:
        x.append(cordinate[0])
        y.append(cordinate[1])
    plt.plot(x, y)

with open('testData.csv', newline='') as csvfile:    
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
        print(pattern)
        plotPath(pattern)
        #print(row["PATTERN"].split(", "))        
plt.show()