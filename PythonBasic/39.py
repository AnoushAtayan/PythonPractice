# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

def future_value(amount, interest, years):
    return amount*(1+interest/100)**years

print future_value(10000, 3.5, 7)