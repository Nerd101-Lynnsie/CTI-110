#Zaria Hill - Sept. 23, 2025 - P2Lab1
#Use the given radius to calculate circle attributes

import math

#Get radius from user
print("What is the radius of the circle? ", end="")
radius = float(input())
print()
#Calculate the diameter
diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}")
print()
#Calculate the circumference
circum = 2 * math.pi * radius
print(f"The circumference of the circle is {circum:.2}")
print()
#Calculate the area
area = math.pi * radius**2
print(f"The area of the circle is {area:.3f}")