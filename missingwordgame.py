#missingwordgame
import random
import time

choices = ["outside", "good", "raincoat"]
print("Welcome to the missing word game!\n")

def question():
    answer = input("\nWhich is the missing word?\noutside\ngood\nraincoat")  
    return answer
#Question1
questionONE = "Is it hot ----- ?"
print(questionONE)
answer = question()
if answer == choices[0]:
    print("Amazing!!")
else:
    print("Try again!")
time.sleep(2)

#Question2
questionTWO = "They got there early, and they got really ------- seats"
print(questionTWO)
answer = question()
if answer == choices[1]:
    print("Amazing!!")
else:
    print("Try again!")
time.sleep(2)

#Question3
questionTHREE = "I accidentally brought my ------- on a sunny day"
print(questionTHREE)
answer = question()
if answer == choices[2]:
    print("Amazing!!")
else:
    print("Try again!")
