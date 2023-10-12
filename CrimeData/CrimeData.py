from email.policy import default
import pprint
from CrimDict import *

pp = pprint.PrettyPrinter(depth=2)
defaultdict = dict()

addtoDict('Test', 'Stealing', '1992', 'New York', defaultdict)


print('Crime Data Report')
print('This is a temporary measure.')



print('Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
menu = input()

while menu != 'q':
    if menu == 'l':
        pp.pprint(defaultdict)
        menu = input('Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
    elif menu == 'a':
        print('Please input the information as followed.')
        addtoDict(input('Please provide the name of the criminal:\n'), input('Please add the crime commited.\n'), input('Please add the date.\n'), input('Location of the crime?\n'), defaultdict)
        menu = input('Added. Please enter from these options; l to look at the list, a to add to the list, or q to quit.')
    else:
        print('Incorrect. Please try again.')
        menu = input()