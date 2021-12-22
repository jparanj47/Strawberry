#INST326 Final Project
#Strawberry

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas as pd
import math
import numpy as np
from collections import Counter

#Terrell Mensah

class Covid_Graph:
    """ This is class is meant to store covid data to create a Covid-19 info graph"""

    def plot_data(self, x1, y1, y2):
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

    #Added self to method
    def get_data(self, data_file):
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


# Alan Chen
# importing the modules
import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd

class State:
    """A class that represents a State object.
    
    Attributes:
        state (string): state name.
        fips (int): FIPS code for state.
        cases (int): total number of cases in the state.
    """
    def __init__(self,state,fips,cases):
        """Initializes the State object.

        Args:
            state (string): see class documentation.
            fips (int): see class documentation.
            cases (int): see class documentation.
        """
        self.state = state
        self.fips = fips
        self.cases = cases
        
    def state_status(self):
        """Identifies the status of the state depending on the number of
            total cases.
            
        Side effects:
            Prints the statement describing the state status and corresponding
                dictionary to console.
        """
        severe = {}
        moderate = {}
        low = {}
        
        if self.cases > 1000000:
            severe[self.fips] = self.state
            print(f"{self.state} has been at severe risk from COVID-19.")
            print(severe)
            
        elif self.cases > 500000:
            moderate[self.fips] = self.state
            print(f"{self.state} has been at moderate risk from COVID-19.")
            print(moderate)
            
        else:
            low[self.fips] = self.state
            print(f"{self.state} has been at low risk from COVID-19.")
            print(low)
                        
def top_state_cases(filepath): 
    """Filters the states with the most covid cases which are flagged as potential hotspots.
    
    Args:
        filepath (string): the path to a file containing U.S. state covid data.
    
    Side effects:
        Displays the filtered database in the console.
    """
    # read in csv file to convert to dataframe
    state_data = pd.read_csv(filepath,index_col="fips")
    
    top_states =  state_data[state_data["cases"] > 1000000]
    display(top_states)

def bar_graph(filepath):
    """Reads a .csv data file and displays the data as a bar graph with proper x 
    and y-axis formatting.
    
    Args:
        filepath (string): the path to a file containing U.S. state covid data.
    """
    state_data = pd.read_csv(filepath)
    
    # x and y variables for states and total cases
    x = list(state_data.loc[:,"state"])
    y = list(state_data.loc[:,"cases"])
    
    plt.bar(x,y,color="green")
    plt.xticks(rotation=90)
    plt.title("COVID-19 Total Cases from 03/01/20 - 12/20/21")
    plt.xlabel("U.S. States/Territories")
    plt.ylabel("Total number of cases (in millions)")
    
    # display bar graph
    plt.show()

# individual functions/methods are called here
def main():
    bar_graph("us-states.csv")
    top_state_cases("us-states.csv")
    state1 = State("Maryland",24,621453)
    state1.state_status()
    state2 = State("California",6,5227931)
    state2.state_status()
    
# main function called here
if __name__ == "__main__":
    main()
  
  
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

from matplotlib import pyplot as plt
import pandas as pd
import re 

class Death1:
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

class Deaths:    
    def __init__(self, deaths, counties):
        """ Creates instances of the class object. 
        Args:
            deaths(int): Number of deaths by county.
        """
        self.deaths = deaths
        self.counties = counties
        
    def parse_deaths(self): 
        """Parsing numbers of deaths after finding regex.
        """
        pattern =r"""(\d+\,\d+)$"""
        match = re.search(pattern, self.deaths)
        return (match.group(1))   
     
    def read_books (filepath):
        """Opens file for reading and then returns a new list of deaths per county.
        Args: 
            filepath(str): path to a file book information. 
            
        Returns:
            list of the numbert of deaths. 
        """
        list_of_deaths = list()
        with open (filepath, "r", encoding = "UTF-8") as file:
            for line in file:
                counties, deaths = line.strip("\t") 
                all_deaths = deaths 
                list_of_deaths.append(all_deaths)
                return list_of_deaths
