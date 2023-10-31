

class CrimeDict:
    
    
    def __init__(self, counter = 1, dictionary = None):
        if dictionary is None:
            dictionary = {0: {'Name':'Test', 'Gender':'Male', 'Date of':'1995', 'Location':'New York', 'Age':'25', 'Status':'Out'}}
        self.counter = counter
        self.dictionary = dictionary
    
    
    def addtoDict(self, name, gender, dateof, location, age, status):
        adddict = {self.counter:{'Name':name, 'Gender':gender, 'Date of':dateof, 'Location':location, 'Age':age, 'Status':status}}

        self.dictionary[self.counter] = adddict[self.counter] 
        self.counter = self.counter + 1


    def searchDict(self, dictionary, search):
        for a in dictionary:
            if search in a:
                print('Found in', a)


        
        
