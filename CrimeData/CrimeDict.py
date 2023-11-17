import csv
import pandas as pd
from pandastable import Table, TableModel

class CrimeDict:
    
    
    def __init__(self, counter = 1, dictionary = {}):
        self.counter = counter
        self.dictionary = dictionary
        self.csvData = ''
    
    def addRecord(self, arrest_key = 0, arrest_date = '1/1/1999', pd_cd = 0, pddesc = 'Default', ky_cd = 0, ofns_desc = 'Default', law_code = 'Default', law_cat_cd = 'D', arrest_boro = 'D', arrest_precint = 0, jurisdiction_code = 0, age_group = 0, perp_sex = 'D', perp_race = 'Default', x_cord = 0, y_cord = 0, latitude = 0, longitude = 0):
        adddict = {self.counter:{'Arrest Key':arrest_key, 'Arrest Date':arrest_date, 'PD CD':pd_cd, 'PD Desc':pddesc, 'ky cd':ky_cd, 'ofns desc':ofns_desc, 'Law Code':law_code, 'Lat Category CD':law_cat_cd, 'Arrest Borough':arrest_boro, 'Arrest Precint':arrest_precint, 'Jurisdiction Code':jurisdiction_code, 'Age Group':age_group, 'Gender':perp_sex, 'Race':perp_race, 'X Cord':x_cord, 'Y Cord':y_cord, 'Latitude':latitude, 'Longitude':longitude}}
        self.dictionary[self.counter] = adddict[self.counter]
        self.counter = self.counter + 1
    
    def importCSV(self, csv_file_path):
            with open(csv_file_path, mode='r') as file:
                rowreader = csv.DictReader(file)
                for row in rowreader:
                    self.dictionary[self.counter] = row
                    self.counter += 1
                    
                    
    
            self.csvData = pd.read_csv(csv_file_path)
    def findRecord(self, category, searchitem):
        sr = pd.DataFrame(self.csvData)
        search = (sr[category] == searchitem)
        print(sr.loc[search])
        
    


        
        
