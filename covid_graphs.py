#Terrell Mensah
#Final Project Check-in 1
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
import math
import numpy as np


def get_data(data_file):
    """ This function is meant to read in the data file
        Args:
            data_file: csv file containing maryland covid data
    """
    #set data equl to pandas.read_csv('data')
    data = pd.read_csv(data_file)
    #set column names = data['column_names']
    date = data['date']
    deaths = data['death']
    recovered = data['recovered']
    #create arrays for data plotting
    deathArr = []
    recoveredArr = []
    months = []
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
    plot_data(monthsArr, deathArr, recoveredArr)

def plot_data(x1, y1, y2):
    """ This function is meant to plot data in a matplotlib graph
        Args:
            x1: months during the pandemic
            y1: the number of deaths of covid patients during the pandemic
            y2: the number of recovered of covid patients during the pandemic

        Returns: Figure 1 - 'Covid deaths compared to recovred patients'
    """
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

get_data('maryland-covid.csv')