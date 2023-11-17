from email.policy import default
from CrimeDict import *
from pandas import DataFrame
from pandas import *
from tkinter import filedialog, messagebox, ttk
from tkinter import *
from pandastable import Table, TableModel, config


root = Tk()



menu = Menu(root)
item = Menu(menu)

root.config(menu=menu)



frame = Frame(root)
frame.pack(fill=BOTH,expand=1)
tabledata = TableModel.getSampleData()
table = pt = Table(frame, dataframe=tabledata, showtoolbar=False, showstatusbar=True)

#tree = ttk.Treeview(frame)
#tree.place(relheight=1, relwidth=0.5)
#treescrollx = Scrollbar(frame, orient="vertical", command=tree.xview_scroll)
#treescrolly = Scrollbar(frame, orient="horizontal", command=tree.yview_scroll)
#tree.configure(xscrollcommand=treescrollx, yscrollcommand=treescrolly)
#treescrollx.pack(side="bottom", fill="x")
#treescrolly.pack(side="right", fill="y")


def findFile():
    
    fileoptions = (("xlsx files", "*.xlsx"),("json files", "*.json"),("csv files,", "*.csv"),("All Files", "*.*"))
    filelocation = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=fileoptions)
    
    loadFile(filelocation)

    return None

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
    table = pt = Table(frame, dataframe=tabledata, showtoolbar=False, showstatusbar=True)
    tabledata = dataf
    table.update()
    table.redraw()    
    return None
        
    

item.add_command(label='Load File', command= findFile)
menu.add_cascade(label='Menu', menu=item)

# Creates the application window with tkinter, root being the application.


# Creates a menu bar with 'File as the menu cascade, and a single command to load a file.


openfile = LabelFrame(root, text='Open File')
openfile.place(height=100, width=400, rely=0.65, relx=0)

label_file = Label(openfile, text="No File Selected")
label_file.place(rely=0, relx=0)
table.show()


# pt.show
# pt.importCSV('C:\\CO-ST\\CrimeData\\CrimeData\\NYPD.csv')

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
        
