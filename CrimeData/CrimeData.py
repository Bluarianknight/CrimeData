from email.policy import default
import pprint
from CrimDict import *

pp = pprint.PrettyPrinter(depth=2)

Crime = CrimeDict()

Crime.addtoDict('Test', 'M', 'Stealing', '1992', 'New York','Released')


print('Crime Data Report')
print('This is a temporary measure.')

def menu():
    print('Please enter from these options; l to look at the list, a to add to the list, or q to quit.')


menu()
sel = input()

while menu != 'q':
    if menu == 'l':
        pp.pprint(Crime.dictionary)  
        menu = input('Provided. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
        print(Crime.counter)
    elif menu == 'a':
        print('Please input the information as followed.')
        Crime.addtoDict(input('Please provide the name of the criminal:\n'), input('Gender?\n'), input('Please add the date.\n'), input('Location of the crime?\n'), input('Age?\n'), input('Status?\n'))
        menu = input('Added. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
    else:
        print('Incorrect. Please try again.')
        menu = input()
        
