#!/usr/bin/python3

"""Print the numbers of 1 to 100 separated by a space
   Print FizzBuzz for numbers which are multples of both three and five
   Print Fizz for numbers which are multiples of three
   Print Buzz for multiples of five
   Print number for the rest
   """

def fizzbuzz():
    for fz in range(1, 101):
        if fz % 3 == 0 and fz % 5 == 0:
            print("FizzBuzz ", end="")
        elif fz % 3 == 0:
            print("Fizz ", end="")
        elif fz % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(fz), end="")
