# Student: Caroline Eliasson

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
# This has a String value stating that "if" the release year is 2019, write "Label: Big Beats Records".
if 2019:
    print('Label: BigBeats Records')

"""
This generates a 2 boolean values, one True and on False. I have created a boolean that simply verifies that 3*3+3=12 (True) and that there is no letter "z" in the name
Andy Grammer (False).
"""

print((3*3)+3==12)
print("z" in "Andy Grammer")