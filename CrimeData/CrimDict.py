
def addtoDict(name, crime, dateof, location, dict):
    adddict = {'Name':name, 'Crime':crime, 'Date of':dateof, 'Location':location}
    dict.update(adddict)
    
def searchDict(dict, search):
    for a in dict:
        if search in a:
            print('Found in', a)
        
    
