#Write a Python program which accepts the radius of a circle from the user and compute the area
import math
def area_circle(input):

    area = math.pi*input**2
    return area

print area_circle(input('Please enter positive integer for radius '))
