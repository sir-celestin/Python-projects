# Determining triangles with sides
# Celestin Nahimana
# April 2024
from math import sqrt


a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

s = (a+b+c)/2

if (s > a ) and (s>b) and (s > c) :
    
    area = round(sqrt(s*(s-a)*(s-b)*(s-c)),2)
    print(f"The area of the triangle with sides of length {a} and {b} and {c} is {area}.")
else : 
    print("Error: The input does not describe a triangle.")


