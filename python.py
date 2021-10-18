import time
import random

name = input("\nHello, what is your name? ")

time.sleep(2)
print("Hello " + name)

feeling = input("\nHow are you today? ")

time.sleep(2)
if "good" in feeling:
    print("\nI'm feeling good too!")
else:
    print("\nI'm sorry to hear that!")
time.sleep(2)
game = input("\nWhich is your favourite game ")
if "pubg" in feeling:
    print("\nOk " + game + " Is a good game ")
else:
    print("\nHaha\n You are biggest noob you know")

age = input("\nwhat is your age ?")
print("\nOk I will remeber your age is "+ age)
time.sleep(2)
anything=input("\nAsk me anything\n I know everything about you \n like name,age,game ")
anything=[name,age,game]
time.sleep(2)
print("\nAnswer is " + random.choice(anything))
print("\nWhat do you think i Answer wrong")
print("\nI am busy \n I will talk to you later\nBye Good Day!!!")