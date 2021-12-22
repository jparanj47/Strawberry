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