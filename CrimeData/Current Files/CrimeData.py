# The project uses three different libraries to handle the database and GUI creation. It uses tkinter for the GUI creation, as it is a library for application creature. 
# We also use pandas, a database library, to load the files and handle the database, and pandastable is used to allow the pandas database to seamlessly
# be implemented into a tkinter GUI.

from email.policy import default
from CrimeDataframe import * # Used to handle and return the database.
from pandas import DataFrame # If it wasn't imported specifically, it wouldn't work. 
from pandas import *
from tkinter import filedialog, messagebox, ttk # Same reason as above - certain commands require it to load specifically.
from tkinter import *
from tkinter.filedialog import asksaveasfile
from pandastable import Table, TableModel, config





class GUI(Frame): # The GUI class inherits the Frame class from tkinter.
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        # Creates the root application window, setting it to 1280 to 720.
        self.root = self.master
        self.root.geometry("1280x720")
        self.CrimeData = CrimeDataframe()
        self.root.title("Crime Data Analyzer")
        # Creates the menu bar at the top of the application.
        self.menu = Menu(self.root)
        self.export = Menu(self.menu)
        self.item = Menu(self.menu)
        self.root.config(menu=self.menu)
        
        # Creates two frames - one to contain the pandastable table, and the other for either rich text or button prompts - unsure yet.
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)
        self.CrimeData.setData(TableModel.getSampleData())
        self.table = Table(self.frame, dataframe=self.CrimeData.outputData(), showtoolbar=False, showstatusbar=False)
        
        
        # Adds the findfile function to the Load File option. 
        self.item.add_command(label='Load File', command= self.findFile)
        self.menu.add_cascade(label='Menu', menu=self.item)
        self.menu.add_cascade(label='Export', menu=self.export)
        self.export.add_command(label='Save as CSV', command=self.saveFileAsCSV)
        self.export.add_command(label='Save as JSON', command=self.saveFileAsJSON)
        self.export.add_command(label='Save as Excel', command=self.saveFileAsExcel)

        #Shows the table, required. 
        self.table.show()
        return

    # Handles the file dialog to obtain file location, before sending it to loadfile(). Handles error exceptions.
    # Referenced https://gist.github.com/RamonWill/0686bd8c793e2e755761a8f20a42c762#file-tkinterexcel-py-L71 for this, alongside
    # https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/ helped as well to figure out some issued I had. 
    def findFile(self):
        
        
        fileoptions = (("csv files,", "*.csv"),("xlsx files", "*.xlsx"),("json files", "*.json"),("All Files", "*.*"))
        filelocation = filedialog.askopenfilename(initialdir="/",
                                            title="Select A File",
                                            filetype=fileoptions)
        try: # Handles any errors if the user picks an invalid file location, or a wrong file type. 
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
        if filepath[-5:] == '.xlsx': # This if/else statement checks to see what type of file it is, and loads the data based on the type.
            dataf = pd.read_excel(filepath)
        elif filepath[-5:] == '.json':
            dataf = pd.read_json(filepath)
        else:
            dataf = pd.read_csv(filepath)
        
        # The CrimeData class is then updated with the data, and then the data is updated on the GUI table. 
        self.CrimeData.setData(dataf)
        self.table.updateModel(TableModel(self.CrimeData.outputData()))
        self.table.update()
        self.table.redraw()    
        return None
    
    def saveFileAsCSV(self): # Allows users to save the data to a csv file, using asksaveasfile to open a save file prompt.
        tableData = self.CrimeData.outputData()
        location = asksaveasfile(initialfile= 'CrimeData.csv', defaultextension='.csv', filetypes=[("All Files", "*.*"), ("CSV Files", "*.csv")])
        tableData.to_csv(location)  
        
    def saveFileAsJSON(self): # Allows users to save the data to a json file, using asksaveasfile to open a save file prompt.
        tableData = self.CrimeData.outputData()
        location = asksaveasfile(initialfile= 'CrimeData.json', defaultextension='.json', filetypes=[("All Files", "*.*"), ("JSON Files", "*.json")])
        tableData.to_json(location)
    
    def saveFileAsExcel(self): # Allows users to save the data to a excel file, using asksaveasfile to open a save file prompt.
        tableData = self.CrimeData.outputData()
        location = asksaveasfile(initialfile= 'CrimeData.xlsx', defaultextension='.xlsx', filetypes=[("All Files", "*.*"), ("CSV Files", "*.xlsx")])
        tableData.to_excel(location)
    

# Initiates the GUI class.
y = GUI()
y.mainloop()