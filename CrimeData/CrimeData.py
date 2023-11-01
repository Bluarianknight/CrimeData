from email.policy import default
import pprint
from CrimeDict import *

pp = pprint.PrettyPrinter(depth=2)

Crime = CrimeDict()
Crime.addRecord()
Crime.importCSV('C:\\CO-ST\\CrimeData\\CrimeData\\NYPD.csv')

print('Crime Data Report')
print('This is a temporary measure.')

def menu():
    print('Please enter from these options; l to look at the list, a to add to the list, or q to quit.')

def newDict():
    a = input('Please provide the name of the criminal:\n'), input('Gender?\n'), input('Please add the date.\n'), input('Location of the crime?\n'), input('Age?\n'), input('Status?\n')

menu()
sel = input()

while menu != 'q':
    if menu == 'l':
        pp.pprint(Crime.dictionary)  
        menu = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
        print(Crime.counter)
    elif menu == 'a':
        Crime.addRecord(input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input(),input())
        menu = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
    else:
        print('Incorrect. Please try again.')
        menu = input()
        
