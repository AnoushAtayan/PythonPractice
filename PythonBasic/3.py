#Write a Python program to display the current date and time.
import datetime

currentTime = datetime.datetime.now()

print ('Current date and time : ')
print (currentTime.strftime('%Y-%m-%d %H:%M:%S'))