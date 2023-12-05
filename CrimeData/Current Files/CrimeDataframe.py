import csv
import pandas as pd
from pandastable import Table, TableModel

# This class handles the pandas dataframe used in the program.
class CrimeDataframe:
    
    def __init__(self, data = pd.DataFrame):
        self.Data = data # Sets the data as a default dataframe, if none is provided.
        
    def setData(self, data): # Sets the Data to the dataframe provided.
        self.Data = data
        
            
    def outputData(self): # Returns the dataframe. 
        return self.Data
    


    
    
