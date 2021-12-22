import matplotlib.pyplot as plt
import csv

x = []
y = []
def deathPerCountyGraph(csvData):
    with open(csvData) as csvFile:
        plot = csv.reader(csvFile, delimiter = ',')
        
        for row in plot:
            x.append(row[0])
            y.append(int(row[2]))
            
    plt.bar(x, y, color = 'g', width = 0.72, label = "Deaths")
    plt.xlabel('Dates')
    plt.ylabel('Death count')
    plt.title('Death count per Date')
    plt.legend()
    plt.show()
        
deathPerCountyGraph('maryland-covid.csv')