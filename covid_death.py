#Gerald Boateng
#check-in 1

from matplotlib import pyplot as plt
import pandas as pd

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
    
def max_deaths (self, df):
     """ Creates a new dataframe for deaths greater than 2000 per state.
        Args:
            ef: file to be read in. 
    """

    filter_deaths = df(df["Deaths"] > 2000) & (df.groupby("State"))
    
    return filter_deaths
    