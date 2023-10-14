

class CrimeDict:
    counter = 0
    dict = dict()
    
    
    def addtoDict(self, name, gender, dateof, location, age, status):
        adddict = {}

        dict.update({self.counter:{'Name':name, 'Gender':gender, 'Date of':dateof, 'Location':location, 'Age':age, 'Status':status}})
        self.counter = self.counter + 1

    def searchDict(self, dict, search):
        for a in dict:
            if search in a:
                print('Found in', a)


        
        
