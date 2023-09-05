import pyttsx3
command = pyttsx3.init()
voices = command.getProperty('voices')
for voice in voices:
    print("Voice:", voice.name)


def speak():
    lang_choice = input("Enter the language code (e.g., en for English, es for Spanish,ar for arabic): ")

speak()



print("Welcome to your personal speaker")
print("type # to exit")

while True:
        a = input("type your thoughts here")
        if a == "#":
            command.say("goodbye , my friend")
            command.runAndWait()
            break
        command.say(a)
        command.runAndWait()








