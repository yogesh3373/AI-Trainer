import ctypes
import subprocess
import pyttsx3
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime
import time
import random
import os
import cv2
import numpy as np
import time
import PoseModule as pm
import requests
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import sys
import self
def righthand():
    cap = cv2.VideoCapture(0)

    detector = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        # img = cv2.imread("AiTrainer/test.jpg")
        img = detector.findPose(img, False)

        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
            # Right Arm
            angle = detector.findAngle(img, 12, 14, 16)
            # # Left Arm
            # angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (210, 310), (0, 100))
            bar = np.interp(angle, (220, 310), (650, 100))
            # print(angle, per)

            # Check for the dumbbell curls
            color = (255, 0, 255)
            if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)

            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)

            # Draw Curl Count
            cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
def lefthand():
    cap = cv2.VideoCapture(0)

    detector = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        # img = cv2.imread("AiTrainer/test.jpg")
        img = detector.findPose(img, False)

        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
            # Right Arm
            # angle = detector.findAngle(img, 12, 14, 16)
            # # Left Arm
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (210, 310), (0, 100))
            bar = np.interp(angle, (220, 310), (650, 100))
            # print(angle, per)

            # Check for the dumbbell curls
            color = (255, 0, 255)
            if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)

            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)

            # Draw Curl Count
            cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def take_screenshot():
    speak("sir, please tell me the name of the screenshot")
    name = takecommand()
    speak("im taking screenshot")
    # time.sleep(1)
    ing = pyautogui.screenshot()
    ing.save(f"{name}.png")
    speak("I am done sir")

def spotify():
    speak("Here your favourite music player is opening Sir")
    webbrowser.open("https://open.spotify.com/")

def whatapp():
    speak("Here your go Sir Whatsapp is Opening")
    webbrowser.open("www.whatsapp.com")

def google():
    speak("what should I search on google, sir")
    qn = takecommand().lower()
    webbrowser.open(qn)

def yahoo():
    speak("what should I search on yahoo")
    qn = takecommand().lower()
    webbrowser.open()

def wiki():
    speak("What you want to search on wikipedia")
    qn = takecommand().lower()
    result = wikipedia.summary(qn, sentences=2)
    speak("According to wikipedia {result}")
    print(result)

def play_yt():
    speak("what is the content of video you needed sir")
    name = takecommand()
    speak("playing" + name)
    pywhatkit.playonyt(name )

def YouTube():
    speak(" Here you go sir Enjoy the million video on Youtube platform")
    webbrowser.open("www.youtube.com")

def amazon():
    speak("opening amazon for you sir buy your fav items here")
    webbrowser.open("https://www.amazon.in/")

def flipkart():
    speak("opening flipkart for you sir buy your fav items here")
    webbrowser.open("https://www.flipkart.com/")

def twitter():
    speak("Here you go sir Twitter is opening in a few sec sir, Expose your thoughts with twit")
    webbrowser.open("https://twitter.com/")

def instagram():
    speak("Here you go sir most of the peoples choice Instagram is opening now sir")
    webbrowser.open("https://www.instagram.com/")

def FaceBook():
    speak("Opening Facebook")
    webbrowser.open("www.facebook.com")

def wynkmusic():
    speak("Here your favourite music player is opening Sir")
    webbrowser.open("https://wynk.in/")

def gaana():
    speak("Here your favourite music player is opening Sir")
    webbrowser.open("https://gaana.com/")

def  netflix():
    speak("Here your favourite entertainer netflix is opening Sir")
    webbrowser.open("https://www.netflix.com/in")

def  primevideo():
    speak("Here your favourite entertainer amazon prime video is opening Sir")
    webbrowser.open("https://www.primevideo.com/")

def disneyhotstar():
    speak("Here your favourite entertainer disney+hotstar is opening Sir")
    webbrowser.open("https://www.hotstar.com/in")

def telegram():
        speak("Here your favourite messenger is opening Sir")
        webbrowser.open("https://web.telegram.org/")

def github():
    speak("Here your progammer site github is opening Sir")
    webbrowser.open("https://github.com/")

def zomato():
    speak("Here your food ordering site zomato is opening Sir")
    webbrowser.open("https://www.zomato.com/")

def swiggy():
    speak("Here your food ordering site swiggy is opening Sir")
    webbrowser.open("https://www.swiggy.com/")

def ola():
    speak("Here your taxi service ola is opening Sir")
    webbrowser.open("https://www.olacabs.com/")

def uber():
    speak("Here your taxi service uber is opening Sir")
    webbrowser.open("https://www.uber.com/")

def music():
    music_dir = "C:\\Users\\rprad\\Downloads\\music"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir, rd))
    speak("here is your favourite music playlist")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening...")
        audio = r.listen(source, timeout=4, phrase_time_limit=7)
        r.pause_threshold=1

        try:
            print("Recognizing")
            query=r.recognize_google(audio, language= 'en-in')
            print(query)

        except Exception as e:
            # speak("Sorry sir, say that again please")
            return "none"
        query = query.lower()
        return query

def hello():
    speak("hello sir, how are you feeling right now sir")

def hi():
    speak("hi sir, and.. how was your day sir")

def day():
    speak("my every day always depends on you sir, you know one thing sir i expecting that when you are going to power on my system")

def how():
    speak("my system running well, and im fine, how are you sir")

def fine():
    speak("it's great to hear from you sir")

def understand():
    speak("will you listen to what the FUCK i said")

def call():
    speak("call me as FRIDAY")

def angry():
    speak("if you had a reason to angry at me, absolutely you can scold me otherwise i will scold you")

def fileexplorer():
    speak("Opening File Explorer")
    os.system("start File Explorer")

def close_fileexplorer():
    speak("closing File Explorer")
    os.system("taskkill /f /in File Explorer.exe")

def cmd():
    speak("opening command prompt")
    os.system("start cmd")

def close_cmd():
    speak("closing cmd")
    os.system("taskkill /f /in cmd.exe")

def ipaddress():
    ip = requests.get("https://api.ipify.org/").text
    speak(f"your ip address is {ip}")

def wish():
    hour = int(datetime.datetime.now().hour)
    tt= time.strftime("%I %M %p")

    if 4 <= hour <= 12:
        speak("im online sir")
        a= "Morning Sir ", "Good Morning sir"
        speak(random.choice(a) +  "It is "  + tt)

        b = "it's pleasant day out there", "Wakeup Sir", "Enjoy the Day sir"
        speak("Sir" + random.choice(b))

    elif 12 <= hour < 16:
        speak("im online sir")
        a = "Good noon sir ", "Good Afternoon sir"
        speak(random.choice(a) +  "It is "  + tt)

        b = "sun shines very well", "it's sunny Sir", "get ready for outing sir"
        speak("Sir" + random.choice(b))

    elif 16 <= hour < 21:
        speak("im online sir")
        a = "Good Evening sir ", "evening sir"
        speak(random.choice(a) + "It is" + tt)

        b = "you are looking tired", "had a snack sir"
        speak("Sir" + random.choice(b))

    else:
        speak("im online sir")
        a = "Good Night sir, Sir ", "Hello Sir, Good Night sir "
        speak(random.choice(a) +  "It is "  + tt)

        b = "time to sleep sir", "Go to bed Sir", "take some rest sir"
        speak("Sir" + random.choice(b))
def squatpush():
    os.system("py SquatPush.py")
def stop():
        f = "As your wish, Sir", "okay sir im going offline", "please call me soon sir"
        speak(random.choice(f))
        exit(0)
def detectemotion():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Clearing background noise...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Waiting for your message...')
        recordedaudio = recognizer.listen(source)
        print('Done recording...')
    try:
        print('print message..')
        text = recognizer.recognize_google(recordedaudio, language='en-US')
        print('Message:{}'.format(text))
    except Exception as ex:
        print(ex)

    Sentence = [str(text)]
    analyser = SentimentIntensityAnalyzer()
    for i in Sentence:
        v = analyser.polarity_scores(i)
        print(v)


def TaskExecution(slef=None):
    wish()
    while True:
        query = takecommand().lower()

        if "open file explorer" in query:
            fileexplorer()

        elif 'lock' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'shutdown the system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call("shutdown", "p /f ")

        elif"open cmd" in query:
            cmd()

        elif "close File Explorer" in query:
            close_fileexplorer()

        elif "close cmd" in query:
            close_cmd()
        elif "mood" in query:
            detectemotion()

        elif "ip address" in query:
            ipaddress()

        elif "play music" in query:
            music()

        elif "open youtube" in query:
            YouTube()

        elif "open facebook" in query:
            FaceBook()

        elif "open yahoo" in query:
            yahoo()

        elif "open google" in query:
            google()

        elif "search on wikipedia" in query:
            wiki()

        elif "open whatsapp" in query:
            whatapp()

        elif "open Twitter" in query:
            twitter()

        elif "play on youtube" in query:
            play_yt()
        elif "training push" in query:
            squatpush()

        elif "open instagram" in query:
            instagram()

        elif "open spotify" in query:
            spotify()

        elif "open flipkart" in query:
            flipkart()

        elif "open amazon" in query:
            amazon()

        elif "open wynk music" in query:
            wynkmusic()

        elif "open netflix" in query:
            netflix()

        elif "open prime video" in query:
            primevideo()

        elif "open disney hotstar" in query:
            disneyhotstar()

        elif "open telegram" in query:
            telegram()

        elif "open github" in query:
            github()

        elif "open zomato" in query:
            zomato()

        elif "open swiggy" in query:
            swiggy()

        elif "open ola" in query:
            ola()

        elif "open uber" in query:
            uber()

        elif "hello friday" in query:
            hello()

        elif "hi friday" in query:
            hi()

        elif "how was your day" in query:
            day()

        elif "how can i call you" in query:
            call()

        elif "angry at you" in query:
            angry()

        elif "i can't understand what you said" in query:
            understand()

        elif "screenshot" in query:
            take_screenshot()

        elif "go offline" in query:
            stop()

        elif "how are you" in query:
            how()
        elif "training right" in query:
            righthand()
        elif "training left" in query:
            lefthand()
        elif "I am fine" in query:
            fine()


        elif "thank you" in query:
            speak("you're welcome sir")

        speak(" ")

if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "hello" in permission:
            TaskExecution()
        elif "bye" in permission:
            speak("bye sir, have a good day")
            sys.exit()