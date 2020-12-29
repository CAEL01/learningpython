"""
FizzBuzz Assignment:
Here are the rules for the assignment (as specified by Imran Gory):
Write a program that prints the numbers from 1 to 100. But for 
multiples of three print "Fizz" instead of the number and for the 
multiples of five print "Buzz". For numbers which are multiples of 
both three and five print "FizzBuzz".
"""

for i in range (1,101):                                 # Wrote 101 because count begins on 0
        if i%3 == 0 and i%5 == 0:                       # 3/3 = Fizz and 5/5 = Buzz --> Print FizzBuzz
                print("FizzBuzz")
        elif i%3 == 0:                                  # Numbers divisible by 3 (3/3=0) --> Print Fizz
                print("Fizz")
        elif i%5 == 0:                                  # Numbers divisible by 5 (5/5=0, 15/5 = 0, 30/5=0) --> Print Buzz
                print("Buzz")
        else: print(str(i))
