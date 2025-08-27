#print("Hello Python world!")

#import matplotlib.pyplot as plt
#        print("Matplotlib installed successfully!")
#import os
#print(os.environ["PATH"])
#import this

import math

def squarert(number1):
    try:
        output=math.sqrt(number1)
        print(f"Result: {output}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a floar value.")

number1=float(input("Enter your number:"))
squarert(number1)

        