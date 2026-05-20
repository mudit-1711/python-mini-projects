import pyjokes
import pyttsx3 as tts
engine = tts.init()
user = input("do you want to listen joke ?? (yes/no) : ")
if user == "yes":
    a = pyjokes.get_joke()
    print(a)
    engine.say(a)
    engine.runAndWait()
    user = input("do you want to listen another joke ?? (yes/no) : ")
    while user == "yes":
        a = pyjokes.get_joke()
        print(a)
        engine.say(a)
        engine.runAndWait()
        user = input("do you want to listen another joke ?? (yes/no) : ")
    print("get lost")
else:
    print("get lost")
   
