#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them


user_fname = raw_input("Print your first name ")
user_lname = raw_input("Print your last name ")
print (user_lname+ ' ' + user_fname)


def reverse():
    reverse = ''
    for i in range(0, len(user_lname)):
        reverse+=user_lname[-i-1]
    return reverse

print reverse()


