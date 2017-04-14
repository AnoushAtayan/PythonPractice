#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
import re

def generate():
    user_input = raw_input('Please enter a sequence of comma-separated numbers ')

    integers = re.findall("[0-9]+", user_input)
    print integers
    tup = tuple(integers)
    print tup

generate()


