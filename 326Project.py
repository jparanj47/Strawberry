#INST326 Final Project
#Strawberry

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas as pd
import math
import numpy as np
from collections import Counter

#Terrell Mensah
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


#Alan Chen
""" Display a graph of the total covid cases in all U.S. states and will display
    either a red or green color status for each state.
"""
def readfile(filepath):
    """Reads a csv data file and displays the data as a bar graph with proper x 
    and y-axis formatting.
    
    Args:
        filepath (string): the path to a file containing U.S. covid cases data.
    """
    # initialize DataFrame from reading csv file
    df = pd.read_csv(filepath)
    
    # x and y variables for states and total cases
    x = list(df.loc[:,"state"])
    y = list(df.loc[:,"cases"])
    
    plt.bar(x,y,color="green")
    plt.xticks(rotation=90)
    plt.title("COVID-19 Total Cases from 03/01/20 - 11/14/21")
    plt.xlabel("States/Territories")
    plt.ylabel("Total number of cases (in millions)")
    
    # display bar graph
    plt.show()

def top_state_cases(df):
    """ Filters the states with the most covid cases and they will have a "red" 
    color status as a potential hotspot. for map
    
    Args:
        df (DataFrame): the DataFrame to be filtered
    
    Returns:
        The states with the most covid cases.
    """
    cases_filter = df["cases"] > 1_000_000
    top_states_df = df[cases_filter]
    cols = ["States", "Total cases"]
    top_states = top_states_df[cols]
    
    return top_states
  
  
#Jay Paranjape
names = []
marks = []
  
f = open('umdCounty.txt','r')
for row in f:
    row = row.split(' ')
    names.append(row[0])
    marks.append(int(row[1]))
  
plt.bar(names, marks, color = 'g', label = 'File Data')
  
plt.xlabel('Student Names', fontsize = 12)
plt.ylabel('Marks', fontsize = 12)
  
plt.title('Students Marks', fontsize = 20)
plt.legend()
plt.show()


#Gerald Boateng
def read_and_create (filepath):
    """ Reads in the data file, creates a new dataframe and plot for deaths per state.
        Args:
            filepath: path to csv file containing covid data
    """
    read_df = pd.read_csv(filepath)
    
    extract_column = ["State", "Deaths"]
    new_df =  read_df[extract_column]
    
    x_axis = list(new_df.loc[:, "State"])
    y_axis = list(new_df.loc[:, "Deaths"])
    
    plt.plot(x_axis, y_axis, c="red")
    plt.xlabel("State")
    plt.ylabel("Number of Deaths")
    plt.title("COVID-19 Deaths per State.")
    plt.show()
    
def max_deaths (df):
     """ Creates a new dataframe for deaths greater than 2000 per state.
        Args:
            df: file to be read in. 
    """

    filter_deaths = df(df["Deaths"] > 2000) & (df.groupby("State"))
    
    return filter_deaths
