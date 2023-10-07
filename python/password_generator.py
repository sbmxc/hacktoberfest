import string
from random import *
from os import sys

def password_create():
    characters= string.ascii_letters + string.punctuation + string.digits
    password="".join(choice(characters) for x in range(randint(8,16)))
    print("Your Password is: {}".format(password))


print("Password Generator")
password_create()
change=input("Do you want another password? Press 'Y' or 'N': ")
print('\n')
while change=='Y' or change=='y':
    password_create()
    change=input("Do you want another password? Press 'Y' or 'N': ")
    print('\n')
else:
    sys.exit()

