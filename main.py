import pyttsx3  # pip install pyttsx3
import datetime  # pip install datetime
import speech_recognition as sr  # pip install speech_recognition
import pyaudio
import wikipedia  # pip install wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import smtplib  # To send email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    print(f"its {Time}")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon Sir")
    elif hour >= 16 and hour < 19:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("I am Jarvis Sri. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

# Function to send email
def send_email(to_email, subject, body):
    from_email = "your_email@gmail.com"  # Replace with your email address
    password = "your_password"  # Replace with your email password or app password if 2FA enabled

    # Set up the MIME object to compose the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        speak("Email sent successfully!")
    except Exception as e:
        speak(f"Failed to send email. Error: {str(e)}")

def TaskExecution():
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching in wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("ok sir opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("ok sir opening google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("ok sir opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query or 'could you play some song' in query:
            speak("ok sir, playing some music")
            music_dir = "C:\\Users\\ashwa\\Music\\Playlists\\mysongs.m3u8\\"
            print(music_dir)
            os.startfile(os.path.join(music_dir))
        elif 'the time' in query:
            speak("ok sir current time is")
            time()
        elif 'the date' in query:
            speak("ok sir current date is")
            date()
        elif 'open code' in query:
            speak("ok sir opening our code")
            codePath = "C:\\Users\\ashwa\\Local\\Programs\\Microsoft VS Code Insiders\\Code - Insiders.exe"
            os.startfile(codePath)
        elif 'temperature' in query:
            search = "weather forecast in Medak"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current weather {search} is {temp}")
        elif 'send email' in query:
            speak("Whom do you want to send the email to?")
            recipient_email = takeCommand().lower()
            speak("What should the subject of the email be?")
            subject = takeCommand().lower()
            speak("What should the body of the email be?")
            body = takeCommand().lower()
            send_email(recipient_email, subject, body)
        elif "how much power is left" in query or "how much power we have" in query or "check up battery level" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f"sir our system have {percentage} percentage")
            speak(f"sir our system have {percentage} percent battery")
        elif "hello" in query or "hey" in query:
            speak("hello sir, may i help you with something?")
        elif "how are you" in query:
            speak("i am fine sir, what about you?")
        elif "also good" in query or "fine" in query:
            speak("that's great to hear from you")
        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure sir.")
        elif "you can sleep" in query or "sleep now" in query:
            speak("okay sir, i am going to sleep you can call me anytime")
            break

if __name__ == "__main__":
    while True:
        permission = takeCommand().lower()
        if "wake up" in permission or "okay jarvis" in permission:
            TaskExecution()
        elif "good bye" in permission:
            sys.exit()
