#Alan Chen
""" Display a graph of the total covid cases in all U.S. states and will display
    either a red or green color status for each state.
"""

import matplotlib.pyplot as plt
import pandas as pd

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
    plt.ylabel("Total number of cases")
    
    # display bar graph
    plt.show()

def top_state_cases(df):
    """ Filters the states with the most covid cases and they will have a "red" 
    color status as a potential hotspot.
    
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
                
readfile("us-states.csv")
yo
