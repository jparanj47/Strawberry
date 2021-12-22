import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
def positiveCasePerCountyGraph(csvData):
    with open(csvData) as csvFile:
        plot = csv.reader(csvFile, delimiter = ',')
        
        for row in plot:
            x.append(row[0])
            y.append(int(row[21]))
            
    plt.bar(x, y, color = 'g', width = 0.72, label = "Cases")
    plt.xlabel('Dates')
    plt.ylabel('Case count')
    plt.title('Case count per Date')
    plt.legend()
    plt.show()

positiveCasePerCountyGraph('maryland-covid.csv')