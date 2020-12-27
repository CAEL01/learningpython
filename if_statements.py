#Function with three parameters using equality. 
def functionCheckEquality(para1, para2, para3):
  """
  para1=int(input("enter any number"))    # Input from external user that I don't define myself. 
  para2=int(input("enter any number"))    # Does not need to be in the code. 
  para3=int(input("enter any number"))    # Variables already defined by myself.
  """
  if para1==para2:                        # Print "True" if this parameter is met.
    print("True: p1 == p2")
    return True
  if para1==para3:                        # Print "True" if this parameter is met.
    print("True: p1 == p3")
    return True
  if para2==para3:                        # Print "True" if this parameter is met.
    print("True: p2 == p3")
    return True
  else:
    print("False")                        # Print "False" if no parameter is equal to any of the other.
    return False
  
value1 = 0                                 # Input that I define the value of.
value2 = 0                                 # When one, or all, of the values are changed, the boolean changes.
value3 = 0                                 # My function defines what parameters will be printed visibly.
                                           # If all values = 0, my function will print out the first parameter
                                           # that stops printing as soon as it has been read by the computer.

functionCheckEquality(value1, value2, value3)   #Calling my function with all my if statements and booleans.
