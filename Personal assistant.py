import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[7].id)  # 23 arabic 33


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'basuony' in command:
                command.replace('basuony', '')
    except:
        pass
    return command


def run():
    command = take_command()
    print (command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f'current time is {time}')
    elif 'who is' in command:
        query = command.replace('who is', '')
        print(query)
        info = wikipedia.summary(query, 1)
        talk(info)
        print(info)
    elif 'what is' in command:
        query = command.replace('who is', '')
        print(query)
        info = wikipedia.summary(query, 1)
        talk(info)
        print(info)
    elif 'what are you' in command:
        talk("my name is Basuony and I'm here to help")
        print("my name is Basuony and I'm here to help")
    elif 'joke' in command:
        x = pyjokes.get_joke()
        talk(x)
        print(x)
    else:
        talk("sorry I counldnt get that")

while True:
    run()
