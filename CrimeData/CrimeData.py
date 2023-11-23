# The project uses three different libraries to handle the database and GUI creation. It uses tkinter for the GUI creation, as it is a library for application creature. 
# We also use pandas, a database library, to load the files and handle the database, and pandastable is used to allow the pandas database to seamlessly
# be implemented into a tkinter GUI.

from email.policy import default
from CrimeDict import * # CrimeDict is used for managing the data in the back - currently not used yet proper as pandastable handles a lot of it.
from CrimeDataframe import *
from pandas import DataFrame # If it wasn't imported specifically, it wouldn't work. 
from pandas import *
from tkinter import filedialog, messagebox, ttk # Same reason as above - certain commands require it to load specifically.
from tkinter import *
from pandastable import Table, TableModel, config


CrimeData = CrimeDataframe()
Crime = CrimeDict()


class GUI(Frame):
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        # Creates the root application window, setting it to 1280 to 720.
        self.root = self.master
        self.root.geometry("1280x720")
        
        # Creates the menu bar at the top of the application.
        self.menu = Menu(self.root)
        self.item = Menu(self.menu)
        self.root.config(menu=self.menu)
        
        # Creates two frames - one to contain the pandastable table, and the other for either rich text or button prompts - unsure yet.
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)
        self.tableData = TableModel.getSampleData()
        self.table = Table(self.frame, dataframe=self.tableData, showtoolbar=False, showstatusbar=False)
        

        self.list = [
            "ARREST_KEY",
            "ARREST_DATE",
            "PD_CD",
            "PD_DESC",
            "KY_CD",
            "OFNS_DESC",
            "LAW_CODE",
            "LAW_CAT_CD",
            "ARREST_BORO",
            "ARREST_PRECINCT",
            "JURISDICTION_CODE",
            "AGE_GROUP",
            "PERP_SEX",
            "PERP_RACE",
            "X_COORD_CD",
            "Y_COORD_CD",
            "Latitude",
            "Longitude",
            "Lon_Lat"
        ]
        
        # Adds the findfile function to the Load File option. 
        self.item.add_command(label='Load File', command= self.findFile)
        self.item.add_command(label="Sort", command= self.popUp)
        self.menu.add_cascade(label='Menu', menu=self.item)

        #Shows the table, required. 
        self.table.show()
        return
        


    def popUp(self):
        self.sortCheckSelect = StringVar()
        self.sortCheckSelect.set("ARREST KEY")
        self.sortCheckSelecttwo = StringVar()
        self.sortCheckSelecttwo.set("ARREST KEY")
        self.sortWindow = Toplevel(self.root)
        self.sortWindow.geometry("720x270")
        self.sortWindow.title("Sorting")
        self.sortButton = Button(self.sortWindow, text="Sort").pack()
        self.sortCheck = OptionMenu(self.sortWindow, self.sortCheckSelect, *list).pack()
        self.sortCheckTwo = OptionMenu(self.sortWindow, self.sortCheckSelecttwo, *list).pack()

    # Handles the file dialog to obtain file location, before sending it to loadfile(). Handles error exceptions.
    # Referenced https://gist.github.com/RamonWill/0686bd8c793e2e755761a8f20a42c762#file-tkinterexcel-py-L71 for this, alongside
    # https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/ helped as well to figure out some issued I had. 
    def findFile(self):
        
        
        fileoptions = (("csv files,", "*.csv"),("xlsx files", "*.xlsx"),("json files", "*.json"),("All Files", "*.*"))
        filelocation = filedialog.askopenfilename(initialdir="/",
                                            title="Select A File",
                                            filetype=fileoptions)
        try:
            self.loadFile(filelocation)
        except ValueError:
            messagebox.showerror("Incorrect File Type!", "You selected an invalid file type.")
            return None
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "The selected file could not be found.")
            return None
        return None

    # Uses the dataf variable as a database to load the file based on it's type, before updating the table with the dataframe. 
    def loadFile(self, filelocation):
        dataf = ''
        filepath = filelocation
        if filepath[-5:] == '.xlsx':
            dataf = pd.read_excel(filepath)
        elif filepath[-5:] == '.json':
            dataf = pd.read_json(filepath)
        else:
            dataf = pd.read_csv(filepath)
        CrimeData.setData(dataf)
        self.table.updateModel(TableModel(dataf))
        self.table.update()
        self.table.redraw()    
        return None
            
        

        

# Redundant code - may be used later, so keeping it. 
# pt.show
# pt.importCSV('C:\\CO-ST\\CrimeData\\CrimeData\\NYPD.csv')

# Everything below this is redundant for a command prompt handling of the data - being kept for testing purposed, 
# and to eventually integrate the code into using the CrimeDict class properly. 




class texting:
    
    def __init__(self):
        print('Crime Data Report')
        print('This is a temporary measure.')
        self.menu()
        self.menuInput()
    
    def menu(self):
        print('Please enter from these options; l to look at the list, a to add to the list, s to search, or q to quit.')

    def menuInput(self):
        self.menu()
        self.sel = input()
        while self.sel != 'q':
            if self.sel == 'l':
                print(Crime.csvData)  
                self.sel = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
                
            elif self.sel == 'a':
                Crime.addRecord(input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input())
                self.sel = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
            elif self.sel == 's':
                Crime.findRecord(input('Input the category.'), input('Input the item you wish to find.'))
                self.sel = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
            else:
                print('Incorrect. Please try again.')
                self.sel = input()
            
    # Concurrently the biggest issue is organization with the code - I plan on creating an application class to handle the application variables, and to clean
    # the code properly. 
    

y = GUI()
y.mainloop()