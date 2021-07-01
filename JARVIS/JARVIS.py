# spaek() == talk()

# importing libraries
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

import pyjokes
import pywhatkit


# listener = sr.recognizer()

# it will initialize the engine to recognize speech
engine = pyttsx3.init('sapi5')
# it will get the voice information
voices = engine.getProperty('voices')
# voices : male (id = 0) & female (id = 1)
print(voices)
print(voices[1].id)
# it will set the voice information
engine.setProperty('voice',voices[1].id)

# it will speak the audio parameter
def speak(audio):
    engine.say(audio) # it will speak the audio
    engine.runAndWait() # it will run and wait

# it is a simple logic method to wish with hour odf the day
def wishMe():
    hour = int(datetime.datetime.now().hour) # it will get the hour of the day
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour <= 0 and hour >=12:
        speak('good afternoon')
    else:
        speak("good evening")
    speak("I am your assistant sir, Please tell me how may I help you")


# it will take microphone input from user and return string output
def takecommand():
    r = sr.Recognizer() # make object of recognizer method of speech_recognition method
    with sr.Microphone() as source: # source microphone
        print("Listining...") # print listening
        r.pause_threshold = 1 # hold for threshold time of 0.5 seconds 
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.record(source, duration = 3) # it listens the source audio and map it in audio string
    try: # if it enable to listen properly then ! error
        print("Recognizing...")
        #   voice = listner.listen(source)
        query = r.recognize_google(audio, language="en-in") # google english india
        print(f"you said: {query} \n ") # it will confirm the query
    except Exception as e: # if it unable to listen properly then error
        print(e) # it print the error

        print("Say that again please...") # it will ask to repeat the audio
        return"None"
    return query # it will return query that is string string format of audio

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # it will help to send email by gmail
    server.ehlo()
    server.starttls()
    server.login("mohitpitti007@gmail.com", "manojpitti001")
    server.sendmail('mohitpitti007@gmail.com',to,content)
    server.close()
    
    
    



if __name__=="__main__":
    wishMe() # it will call wish function
    while True: # it will keep on listening 
    #if 1:
        query = takecommand().lower() # it will assign the string in lower case 
        
        if "wikipedia" in query: # if wikipedia in query audio string then :
            speak("Searching wikipedia...") # speak search wikipedia
            query.replace("wikipedia","")   # it will remove wikipedia by query
            results = wikipedia.summary(query, sentences = 1 ) # it will return 1 sentence
            speak("According to wikipedia") # it will speak then
            print(results) # it will print the results presents in wikipedia
            speak(results) # then it will speak the results sentence returned by wikipedia
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "play movies" in query:
            movie_dir = ""
            movies = os.listdir(movie_dir)
            #print(songs)
#            a = random.randint(1,147)
            os.startfile(os.path.join(movie_dir, movies[1]))
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            
        elif "open file" in query:
            codePath = ""
            os.startfile(codePath)

        elif "open whatsapp" in query:
            webbrowser.open("com.whatsappweb.com")
        
        elif "email to hello" in query:
            try:
                speak('what do you want to speak')
                content = takecommand()
                to = "18ucs124@lnmiit.ac.in"
                sendmail(to, content)
                speak("done!")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send this email...")
        
        elif "thank you bye" in query:
            speak("your welcome i want to get fucked by you sir")
            break