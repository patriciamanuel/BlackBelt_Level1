"""
TASK 2
Patricia Mae M. Manuel
"""


import random
x = random.randint(1, 10)
y = input("Guess the number: ")
y = int(y)

if x == y:
    print ("Correct!")
elif x != y:
    print ("Incorrect")

