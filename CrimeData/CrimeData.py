from email.policy import default
from CrimeDict import * # CrimeDict is used for managing the data in the back - currently not used yet proper as pandastable handles a lot of it.
from pandas import DataFrame # If it wasn't imported specifically, it wouldn't work. 
from pandas import *
from tkinter import filedialog, messagebox, ttk # Same reason as above - certain commands require it to load specifically.
from tkinter import *
from pandastable import Table, TableModel, config


# Creates the root application window, setting it to 1280 to 720.
root = Tk()
root.geometry("1280x720")

# Creates the menu bar at the top of the application.
menu = Menu(root)
item = Menu(menu)

root.config(menu=menu)


# Creates two frames - one to contain the pandastable table, and the other for either rich text or button prompts - unsure yet.
frame = Frame(root)
frametwo = Frame(root)
frame.pack(fill=BOTH,side="right",expand=1)
frametwo.pack(fill=BOTH,side="left",expand=1)
tabledata = TableModel.getSampleData()
table = pt = Table(frame, dataframe=tabledata, showtoolbar=False, showstatusbar=True)



# Handles the file dialog to obtain file location, before sending it to loadfile(). Handles error exceptions.
# Referenced https://gist.github.com/RamonWill/0686bd8c793e2e755761a8f20a42c762#file-tkinterexcel-py-L71 for this, alongside
# https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/ helped as well to figure out some issued I had. 
def findFile():
    
    fileoptions = (("csv files,", "*.csv"),("xlsx files", "*.xlsx"),("json files", "*.json"),("All Files", "*.*"))
    filelocation = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=fileoptions)
    try:
        loadFile(filelocation)
    except ValueError:
        messagebox.showerror("Incorrect File Type!", "You selected an invalid file type.")
        return None
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The selected file could not be found.")
        return None
    return None

# Uses the dataf variable as a database to load the file based on it's type, before updating the table with the dataframe. 
def loadFile(filelocation):
    dataf = ''
    filepath = filelocation
    if filepath[-5:] == '.xlsx':
        dataf = pd.read_excel(filepath)
    elif filepath[-5:] == '.json':
        dataf = pd.read_json(filepath)
    else:
         dataf = pd.read_csv(filepath)
    Crime.csvData = dataf
    table.updateModel(TableModel(dataf))
    table.update()
    table.redraw()    
    return None
        
    
# Adds the findfile function to the Load File option. 
item.add_command(label='Load File', command= findFile)
menu.add_cascade(label='Menu', menu=item)

#Shows the table, required. 
table.show()

# Redundant code - may be used later, so keeping it. 
# pt.show
# pt.importCSV('C:\\CO-ST\\CrimeData\\CrimeData\\NYPD.csv')

# Everything below this is redundant for a command prompt handling of the data - being kept for testing purposed, 
# and to eventually integrate the code into using the CrimeDict class properly. 

print('Crime Data Report')
print('This is a temporary measure.')

Crime = CrimeDict()




def menu():
    print('Please enter from these options; l to look at the list, a to add to the list, s to search, or q to quit.')


menu()
sel = input()

while menu != 'q':
    if menu == 'l':
        print(Crime.csvData)  
        menu = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
        
    elif menu == 'a':
        Crime.addRecord(input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input())
        menu = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
    elif menu == 's':
        Crime.findRecord(input('Input the category.'), input('Input the item you wish to find.'))
        menu = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
    else:
        print('Incorrect. Please try again.')
        menu = input()
        
# Concurrently the biggest issue is organization with the code - I plan on creating an application class to handle the application variables, and to clean
# the code properly. 