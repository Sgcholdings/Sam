import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys 


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            global command
            print('listening .....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Sam' in command:
                command = command.replace('Sam', '')
                print(command)
    except:
        pass
    return command

def run_sam():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        sys.exit()

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk('Current time is ' + time)

    elif 'good morning' in command:
        talk('Good Morning Kudzanai...')

    elif 'goodbye' in command:
        talk('Goodbye ... and thank you....')
        sys.exit()

    elif 'who is' in command:
        wiki = command.replace('who is', '')
        info = wikipedia.summary(wiki, 5)
        print(info)
        talk(info)

    else:
        talk('Please say that command again.')

while True:
    run_sam()