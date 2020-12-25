# Student: Caroline Eliasson

"""
Extra credit:
One of the data types we haven't covered yet is called "booleans". 
When a variable is set to True or False, that's a boolean. For 
extra credit, see if you can figure out how to use booleans, and 
add an extra function that returns a boolean value instead of a 
String or Number. Hint: make sure to capitalize the first letter 
in the words True or False when you use them. We'll cover booleans 
more in the lecture on "if" statements coming up next in the course.
"""

    # Functions

def Genre():
    print('Pop')
Genre()

def Artist():
    print('Andy Grammer')
Artist()

def Song():
    print('Song: I Found You')
Song()

def Year():
    print('Release year: 2019')
Year()

def myYear(year):
    print('Current year: '+year)
myYear("2020")


# Booleans (for extra credit)

# This has a String value stating that "if" the release year is 2019, write (visibly) "Label: Big Beats Records".
if 2019:
    print('Label: BigBeats Records')

"""
This function generates a boolean value of True or False. A boolean can only take two values: True or False. 
I have created a boolean to print that the album has one CD if the value is true or that the album has more than 2 CDs if the value is false.
"""

if True:
    print('Album only contains 1 CD')

if False:
    print('More than 2 CDs in album')