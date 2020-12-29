"""
FizzBuzz Assignment:
Here are the rules for the assignment (as specified by Imran Gory):
Write a program that prints the numbers from 1 to 100. But for 
multiples of three print "Fizz" instead of the number and for the 
multiples of five print "Buzz". For numbers which are multiples of 
both three and five print "FizzBuzz".

        Hint: The one hint you'll likely need is: 
        There is a Python operator called "modulo", represented by the percentage sign
        (%) that gives you the remainder left over after division. So for example:
        6 % 3
        Equals zero. Because after dividing 6 by 3, there is zero leftover. Whereas:
        6 % 4
        Equals 2. Because after dividing 6 by 4, there are 2 left over from the six.
        The point is: the modulo operator is useful for finding out if X is a multiple 
        of Y. If it is, then X % Y will yield zero. Knowing this should help you 
        complete this assignment without any issue.
"""

for i in range (1,101):                                 # Wrote 101 because count begins on 0
        if i%3 == 0 and i%5 == 0:                       # 3/3 = Fizz and 5/5 = Buzz --> Print FizzBuzz
                print("FizzBuzz")
        elif i%3 == 0:                                  # Numbers divisible by 3 (3/3=0) --> Print Fizz
                print("Fizz")
        elif i%5 == 0:                                  # Numbers divisible by 5 (5/5=0, 15/5 = 0, 30/5=0) --> Print Buzz
                print("Buzz")
        else: print(str(i))