from os import name
from webbrowser import Chrome
import pyttsx3
import datetime
import speech_recognition as reg
import wikipedia
import webbrowser
import os
# import Fornt
import subprocess
import pyjokes
import PyPDF2
import pyautogui
# import PIL
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hours = int(datetime.datetime.now().hour)
    if hours >= 0 and hours < 12:
        speak("Good morning sir !")
    elif hours >= 12 and hours <18:
        speak("Good afternoon boss")
    else:
        speak("good evening  Boss")
    speak("wht can i do for u boss")


def takecommand():
    r = reg.Recognizer()
    with reg.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Wait for a few moments")
        query = r.recognize_google(audio, language='en-in')
        print("user said quarry :", query)

    except Exception as e:
        print(e)
        speak("say that again boss")
        return "None"  # None string will be returned
    return query
# def reader ():
#     book = open('book.pdf', 'rb')
#     pdfReader = PyPDF2.PdfFileReader(book)
#     pages = pdfReader.numPages
#     speak(f"ttotal number os pages in the book is {pages}")
#     speak("Enter the page number sir")
#     pg=int(input("Enter the page no sir:"))
#     page = pdfReader.getPage(pg)
#     text = page.extractText()
#     print(text)
#     speak(text)

if __name__ == "__main__":
     wishme()
    #  Fornt
     while True:
 # if 1:
        query =takecommand().lower()
         
        if 'say about' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        elif 'open youtube' in query:           
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            speak("what should i search sir ?")
            cm =takecommand().lower()
            Chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.get(Chrome_path).open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'play music' in query:
            music_dir = 'G:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open code'in query:
            codepath="C:\\Users\\Magesh YT\\AppData\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M") 
            speak(f"Sir, the time is {time}")
        elif "how are you" in query:
            speak("i am fine sir , what about you ?")
        elif "i am fine" in query:
            speak('you will be fine sir i am with you, any other help you need')
        #--------------------------osmodel------------------------------
        elif 'open kali'in query:
           vbpath="C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
           os.startfile(vbpath)
        elif "close the kali" in query:
            os.system("taskkill /f /im VirtualBox.exe")
        elif 'open chrome'in query:
            chromepath="C:\\Program Files\\Google\Chrome\\Application\\chrome.exe" 
            os.startfile(chromepath)
        elif'close the chrome' in query:
             speak("ok sir , closing")
             os.system("taskkill /f /im  chrome.exe")
        #---------------------------------------------------------------------
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by  Magesh.")
        #---------------------joke------------------
        elif 'joke' in query: 
            speak(pyjokes.get_joke())
        elif "about you" in query:
            speak("i am jarvis sir and i am your assistant i can do any work for you")
        elif "close the code" in query:
            speak("closing code sir ")
            os.system("taskkill /f /im Code.exe")
        elif "sleep" in query:
            speak("have a nice sleep sir see you tomorrow")
        #--------------pdf_reader----------------------------
        elif "book" in query:
            book = open('pybook.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak(f"total number is pages in the book {pages}")
            speak("Enter the page number sir")
            pg=int(input("Enter the page no sir:"))
            page = pdfReader.getPage(pg)
            text = page.extractText()
            print(text)
            speak(text)
        #----------------------------screenshot------------------------------
        elif "take"in query:
            speak("sir,please teel the name for the screenshort file")
            name= takecommand().lower()
        
            speak("sir,please hold on ,i am taking screenshort")
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir!")
        #----------------------countdown-------------------
        elif "start" in query:
            speak("set your countdown sir")
            count=int(input("Enter the countdown :"))
            for sec in range(count):
                speak(f"{count-sec} second remining sir")
                
        #----------------------------thankyou------------------------------------------
        elif 'thank you'in query:
         speak("thank you sir have a nice da") 
         break
        
