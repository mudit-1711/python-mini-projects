# 1 snake -1 water 0 gun
import random
user = (input("enter your choise (snake water gun): "))
key = {"snake":1,"water":-1,"gun":0}
revkey = {1:"snake",-1:"water",0:"gun"}
yourkey = key[user]
computer = random.choice([1,-1,0])
print("your choise is : ",user)
print("computer choise is : ",revkey[computer])
if(yourkey == computer):
    print("draw")
elif(yourkey == 1 and computer == -1):
    print("your win")
elif(yourkey == -1 and computer == 1):
    print("computer win")
elif(yourkey == 0 and computer == 1):
    print("your win")
elif(yourkey == 0 and computer == -1):
    print("computer win")
elif(yourkey == -1 and computer == 0):
    print("your win")
elif(yourkey == 1 and computer == 0):
    print("computer win")
