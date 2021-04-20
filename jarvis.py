import pyttsx3
import smtplib
import webbrowser
import wikipedia
import datetime
import os
import speech_recognition as sr
import random





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak('Good Morning sir!')

    elif hour>=12 and hour<18 :
        speak('Good Afternoon Sir!')
    
    else:
        speak('Good Evening Sir!')

    speak('jarvis at your service! how can i help you?')
    

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        # r.energy_threshold = 300  
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")

    except Exception as e:
        print('can you repeat please.')
        return "none"
    
    return query

# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo
#     server.starttls
#     server.login('yourmail@gmail.com', 'your-pass')
#     server.sendmail('sendersmail.ac.in',to, content)
#     server.close




if __name__ == '__main__' :
    
    get_time()
    while True:
    
        query = take_command().lower()
        
        if 'wikipedia' in query :
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =1)
            speak('according to wikipedia')
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            my_dir = 'D:\\mobile data\\songs'
            songs = os.listdir(my_dir)
            # print(songs)
            os.startfile(os.path.join(my_dir,songs[0]))
        
        
        elif 'next song' in query:
            my_dir = 'D:\\mobile data\\songs'
            songs = os.listdir(my_dir)
        
            os.startfile(os.path.join(my_dir,songs[0]))

        elif 'stop music' in query:
            my_dir = 'D:\\mobile data\\songs'
            random.shuffle(songs)
            songs = os.listdir(my_dir)
            

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%I:%M:%S")
            print(strtime)
            speak(f"sir the time is {strtime}")

        # elif 'send email' in query:
        #     try :
        #         speak('what should i write?')
        #         content = take_command()
        #         to = "yadnikthorat@gmail.com"
        #         sendEmail(to, content)
        #         speak('email has been sent')

        #     except Exception as e :
        #         print(e)
        #         speak('error while sending email')
                

