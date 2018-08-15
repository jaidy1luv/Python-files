#To calculate the area of a square
print('Calculating the area of a cylinder:')
from math import pi
r = float(input('Enter the value of radius of the cylinder\n'))
h = float(input('Enter the height of the cylinder\n'))
area = (2 * pi * r * h) + (2 * pi * r**2)
print('The area of the cylinder is\n')
print(round(area, 2))
