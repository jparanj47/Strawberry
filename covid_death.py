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
                

    