import pyttsx3
import speech_recognition as sr


import datetime
import wikipedia
import webbrowser
import os


engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning! mam")
    elif hour>=12 and hour<16:
        speak("Good Afternoon mam")
    else:
        speak("Good Evening mam")
    speak("How may i help you")  
def takeCommand():
    # it takes microphone input from the user and return string output

    r= sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language ='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print("e")
        print("Say that again please..")
        return "None"
    return query
    
     
if __name__ =="__main__":
    wishMe()
    #while True:
    if True:
      
     query=takeCommand().lower()
    
     #logic for executing task based on query
     if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
     elif 'open google' in query:
        webbrowser.open('google.com')
     elif 'open youtube' in query:
         webbrowser.open('youtube.com')   
     elif 'open java t point' in query:
        webbrowser.open('javatpoint.com')
     elif 'play music' in query:
         music_dir='F://songs'
         songs =os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))
     elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"mam, the time is {strTime}")
            print(strTime)
     
     elif 'how are you' in query:
         speak("I am fine, Thank You")
         speak("How are you ,mam")
     elif 'fine' in query or "good" in query:
         speak("It's good to know that your fine")
 
 
     elif "change name" in query:
         speak("What would you like to call me, mam ")
         assname = takeCommand()
         speak("Thanks for naming me")
 
     elif 'exit' in query:
         speak("Thanks for giving me your time")
         exit()
 
     elif "who made you" in query or "who created you" in query: 
         speak("I have been created by Team Flame. Thank You Team Flame.")
     elif 'about to sleep' in query:
         speak("good night mam sweet dreams")
         exit()
     elif "who i am" in query:
         speak("If you talk then definately your human.")
 
     elif "why you came to this world" in query:
         speak("Thanks to Team Flame. They will define me")
     elif "who are you" in query:
         speak("I am your voice assistant.")
 
     elif 'why you was created' in query:
         speak("I was created as a python  project by Team Flame ")
     elif 'shutdown system' in query:
         speak("Hold On a Sec ! Your system is on its way to shut down")
         subprocess.call('shutdown / p /f')
     
 