import csv
import pandas as pd
from pandastable import Table, TableModel


class CrimeDataframe:
    
    def __init__(self, data = pd.DataFrame):
        self.csvData = data
        
    def setData(self, data):
        self.csvData = data
        
    def readData(self, csv_file_path):
        filepath = csv_file_path
        if filepath[-5:] == '.xlsx':
            dataf = pd.read_excel(filepath)
        elif filepath[-5:] == '.json':
            dataf = pd.read_json(filepath)
        else:
            dataf = pd.read_csv(filepath)
            
    def outputData(self):
        return self.csvData
    

class SortedDataframe(CrimeDataframe):
    def __init__(self, data):
        self.csvData = data
        
    def sortDataBy(self, category):
        sortedData = self.csvData.sort_values(by=category, ascending=False)
        return sortedData
    
    def groupBy(self, category, value):
        sortedData = self.csvData.groupby(category)
        return sortedData.get_group(value)