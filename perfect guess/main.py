import random
import pyttsx3 as pytt

engine = pytt.init()

a = int(input("enter your number(between(1,100)): "))
num = random.randint(1,100)

count = 0

while(True):

    if(a < num):
        print("number is lower")

        engine.say("number is lower")
        engine.runAndWait()

        a = int(input("enter higher number : "))

        engine.say("enter higher number")
        engine.runAndWait()

        count += 1

    elif(a > num):
        print("number is higher")

        engine.say("number is higher")
        engine.runAndWait()

        a = int(input("enter lower number : "))

        engine.say("enter lower number")
        engine.runAndWait()

        count += 1

    else:
        print("perfect guess")

        engine.say("perfect guess")
        engine.runAndWait()

        count += 1
        break

print(f"you guessed the number in {count} guesses")

engine.say(f"you guessed the number in {count} guesses")
engine.runAndWait()
