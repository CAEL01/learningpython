"""
Create a function that accepts 3 parameters and checks for equality 
between any two of them. Your function should return True if 2 or 
more of the parameters are equal, and false is none of them are 
equal to any of the others.
"""

# Part 1 of Homework: Function with three parameters using equality (==).

def functionCheckEquality(para1, para2, para3):
#Function with three parameters using equality. 
  if para1==para2:                         # Print "True" if this parameter is met.
    print("True: value1 = value2")
    return True
  if para1==para3:                         # Print "True" if this parameter is met.
    print("True: value1 = value3")
    return True
  if para2==para3:                         # Print "True" if this parameter is met.
    print("True: value2 = value3")
    return True
  else:
    print("False")                         # Print "False" if no parameter is equal to any of the other.
    return False
  
value1 = 1                                 # Input that I, myself, define/write the value of.
value2 = 1                                 # When one, or all, of the values are changed, the boolean changes.
value3 = 0                                 # My function defines what parameters will be printed visibly.
                                           # If all values = 0, my function will print out the first parameter
                                           # that stops printing as soon as it has been read by the computer.

functionCheckEquality(value1, value2, value3)   #Calling my function with all if statements including booleans.

"""
Extra credit:
Modify your function so that strings can be compared to integers if they 
are equivalent. For example, if the following values are passed to your 
function: 6,5,"5" you should modify it so that it returns true instead 
of false. Hint: there's a built in Python function called "int" that will 
help you convert strings to Integers.
"""

# Part 2 of Homework (Extra Credit): Convert all strings to integers.

def functionCompareString(int1,int2,int3):
  int1 = int(int1)
  int2 = int(int2)
  int3 = int(int3)

  if int1 == int2:
    print("True")
    return True
  if int2 == int3:
    print("True")
    return True
  if int3 == int1:
    print("True")
    return True

  print("False")
  return False

value1 = "6"
value2 = "5"
value3 = "5"

functionCompareString(value1,value2,value3)
