#Terrell Mensah
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
import math
import numpy as np

#Create class covid graph
class Covid_Graph:

    def plot_data(self, x1, y1, y2):
        #styling for graphs
        x_indexes = np.arange(len(x1))
        # plot points
        plt.style.use("fivethirtyeight")
        plt.plot(x_indexes, y1, label="Deaths")
        plt.plot(x_indexes, y2, label="Recovered")

        plt.legend()
        plt.xticks(ticks=x_indexes, labels=x1, fontsize=6)
        plt.title("Covid deaths compared to recovered patients")
        plt.xlabel("Years")
        plt.ylabel("Patitents")

        plt.tight_layout()
        plt.show()

    #Added self to method
    def get_data(self, data_file):
        #set data equl to pandas.read_csv('data')
        data = pd.read_csv(data_file)
        #set column names = data['column_names']
        date = data['date']
        deaths = data['death']
        recovered = data['recovered']
        #create arrays for data plotting
        deathArr = []
        recoveredArr = []
        monthsArr = []
        #create for loops to appened new items to lists
        currentMonth = 0
        monthCount = 0
        monthCountArr = []
        for item in date:
            dateList = item.split("-")
            dateList.pop()
            monthDate = int(dateList[1])
            connector = "-"
            newDate = connector.join(dateList)
            if currentMonth != monthDate:
                monthCountArr.append(monthCount)    
                monthCount += 1
                monthsArr.append(newDate)
                currentMonth = monthDate
            else:
                monthCount += 1
        deathCount = 0
        for item in deaths:
            if math.isnan(item):
                item = 0.0
            for num in monthCountArr:
                if deathCount == num:
                    deathArr.append(item)
                    break
            deathCount += 1
        recoveredCount = 0
        for item in recovered:
            if math.isnan(item):
                item = 0.0
            for num in monthCountArr:
                if recoveredCount == num:
                    recoveredArr.append(item)
                    break
            recoveredCount += 1
        monthsArr.reverse()
        deathArr.reverse()
        recoveredArr.reverse()
        #Added self method
        self.plot_data(monthsArr, deathArr, recoveredArr)

    
#Calling method from class
graph = Covid_Graph()
graph.get_data('maryland-covid.csv')