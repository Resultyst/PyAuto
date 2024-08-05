import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os
import datetime
import pyaudio


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Happy Day SuN!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SuN!")
    else:
        speak("Good Evening SuN!") 
    speak("I am Resultyst, How can I help you today?")

def takeCommand():
    s = sr.Recognizer()
    with sr.Microphone() as source:
        print("Trying to hear you....")
        s.pause_threshold = 1
        s.adjust_for_ambient_noise(source) 
        audio = s.listen(source)
    
    try:
        print("Understanding what you said....")
        query = s.recognize_google(audio, language='en-in')
        print(f"SuN said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that. Please say that again.")
        return "None"
    except sr.RequestError:
        print("Sorry, I am having trouble reaching the recognition service.")
        speak("Sorry, I am having trouble reaching the recognition service.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred. Please try again.")
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('@yourgmail.com', 'yourpword')
        server.sendmail('your@gmail.com', to, content)
        server.close()
        speak("Your Email has been sent successfully")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
        speak("Sorry, I am not able to send this email")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'open wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'open notepad' in query:
            npath = "C://Windows//notepad.exe"
            os.startfile(npath)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SuN, the time is {strTime}")
        
        elif 'open resultyst youtube' in query:
            webbrowser.open("https://www.youtube.com/@Resultyst")

        elif 'email to my friend' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                if content != "None":
                    to = "to@gmail.com"
                    sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye SuN! Have a great day!")
            break
