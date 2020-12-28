"""
Create a global variable called myUniqueList. It should be an empty list to 
start. 

Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. If the value doesn't exist 
already, it should be added and the function should return True. If the value 
does exist, it should not be added, and the function should return False; 
Finally, add some code below your function that tests it out. It should 
add a few different elements, showcasing the different scenarios, and then 
finally it should print the value of myUniqueList to show that it worked.

Extra credit:
Add another function that pushes all the rejected inputs into a separate global 
array called myLeftovers. If someone tries to add a value to myUniqueList but 
it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""

myUniqueList=[]                         # Global variable: Empty list.
myLeftOvers=[]                          # Global variable: Empty list for rejected inputs.

def AddToList(newthing):                # Global function: Adds things to list.
    if newthing in myUniqueList:        # If something that already exists in myUniqueList is introduced, print False.
        myLeftOvers.append(newthing)
        return False
    else:
        myUniqueList.append(newthing)   # If something new is presented to myUniqueList, print True.
        return True

print(AddToList("1"))                   # Add 1 to list.
print(AddToList("2"))
print(AddToList("1"))                   # Add 1 again, returns false since value already exists.
print(myUniqueList)                     # Prints everything in my global variable.
print(myLeftOvers)                      # Prints rejected values that are non-unique.
