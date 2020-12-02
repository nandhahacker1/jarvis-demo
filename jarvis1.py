import os
from os import replace
import speech_recognition as sr
import pyttsx3
import datetime
import time
import wikipedia
import webbrowser
import random
import requests# check weather

from pyfiglet import figlet_format
from termcolor import colored

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):#speack function
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" have     a      nice     day    jackson kasi")
    if hour>=12 and hour<18:
        speak(" hai    good    afternoon   jackson kasi")
    elif hour>=18:
        speak("    good    evening   jackson kasi")
    speak(" how   can  i   help   you   sir")

def alarm():
    ti=0
    time=int(datetime.datetime.now().hour)
    while ti<10:  
        if time>=6 and time<7:
            speak(" iniya kalai vanakkam sago eluthiriungal")
        elif time>=12 and time<13:
             speak(" hai    good    afternoon   jackson kasi")
             break
        elif time>=18 and time<19:
            speak(" jackson  kasi     good     evening")
            break
        ti=ti+1

def takeCommand():
    r =  sr.Recognizer()
    with sr.Microphone() as mic:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(mic)
        
    try:
        print("Recognizing...\n")
        # speak(" please     wait     sir")
        query=r.recognize_google(audio,language='en-in')
        print("user said: ",query)
    except Exception as e:
        # print(e)
        # print(" please try again ")
        # speak(" please try again ")
        return "None"
    return query
"""//////////////////////"""

if __name__ == "__main__":
    txt= colored(figlet_format("HELLO JACKSON KASI",font="slant"),color="yellow")
    print(txt)
    # alarm()    
    # wishme()

    while True:
        query = takeCommand().lower()
        if "hey jarvis"in query or "ok jarvis"in query or "jarvis"in query:
            speak(" sir i am ready")

            while True:
                query = takeCommand().lower()

                try:        
#---        ----------------------- The main applications of Google ----------------------------------------
                    # """search"""
                    if 'google' in query:
                        speak('Searching in google...')
                        if "hey" or "hi" or "jarvis"or "jarvish" or "search" or "in" or "on" or "google" in query:
                            a= query.replace("hey", "")
                            b= a.replace("hi", "")
                            c= b.replace("jarvis","")
                            d= c.replace("jarvish","")
                            e= d.replace("search","")
                            f= e.replace("in","")
                            g= f.replace("on","")
                            h= g.replace("google","")

                            source=str(h)
                            print("google searh: ",query,"\n")
                            speak("Search on  Google.com")
                            webbrowser.open(f"https://www.google.com/search?q={source}")
                    #  OR USE  BLOWE FUNC
                    if 'open google' in query:
                        speak("what should i search sir ?")
                        source=takeCommand().lower()
                        webbrowser.open(f"https://www.google.com/search?q={source}")

#---        --------------------- weather today -------------------------
                    elif 'weather tooday' in query:
                        #--------////////////// WEATHER DATA  //////////////----------------
                        speak(" please   sir   tell   your   city   name   or   zip   code   ")
                        location_voice = takeCommand().lower() 
                        location=str(location_voice)
                        try:  
                            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"039785caea4e9adeb529d5b4cfb247b5"
                            api_link = requests.get(complete_api_link)
                            api_data = api_link.json()
                            # create variables to store and display data
                            temp_city = ((api_data['main']['temp']) - 273.15)
                            weather_desc = api_data['weather'][0]['description']
                            hmdt = api_data['main']['humidity']
                            wind_spd = api_data['wind']['speed']
                            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                            country1 = api_data['sys']['country']
                            #-------country set-----------------
                            country2 = "IN"# set your country's
                            def cont():
                                if country1 == country2 :
                                    return("India")
                            #--------////////////// CLOSE WEATHER DATA  //////////////----------------
                            #--------------- weather data detail's output -------------
                            print ("    Today    Weather     Status   ") 
                            print ("location        ".format (location.upper(),     cont()),   date_time)
                            print ("Current temperature is       {:.2f} degree C".format(temp_city))
                            print ("Current weather desc         ",weather_desc)
                            print ("Current Humidity             ",hmdt,'%')
                            print ("Current wind speed           ",wind_spd ,'kmph')
                            #------------------------------------------------------------------
                            speak ("      Today    Weather     Stats      ") 
                            loc1= ("location        ".format (location.upper(),     cont()),   date_time)
                            speak (loc1)
                            loc2= ("Current temperature is       {:.2f} degree   celsius".format(temp_city))
                            speak (loc2)
                            loc3= ("Current weather desc         ",weather_desc)
                            speak (loc3)
                            loc4= ("Current Humidity             ",hmdt, '%')
                            speak (loc4)
                            loc5= ("Current wind speed           ",wind_spd ,'kilometers   per   hour')
                            speak (loc5)

                        except Exception as e:
                            print(e)
                            speak(" please try again")

#---        --------------------- WIKIPEDIA ----------------------------------
                    elif 'wikipedia' in query:
                        speak('Searching in Wikipedia...')
                        if "in" or "Ok" / "wikipedia" / "search" / "wiki" / "jarvis" / "hey" in query:
                            a1=query.replace("ok","")
                            a2=a1.replace("hey","")
                            a=a2.replace("hey","")
                            b= a.replace("jarvis","")
                            c= b.replace("search","")
                            d=c.replace("in", "")
                            e=d.replace("wikipedia", "")
                            query=str(e)
                            print("wiki searh: ",query,"\n")
                            results = wikipedia.summary(query, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

#---        -------------------- OPEN SIMILAR WEBSITE'S ------------------------
                    elif 'open youtube' in query:
                        speak("open youtupe")
                        webbrowser.open("youtube.com")

                    elif 'open stackoverflow' in query or "stack overflow" in query or "stackoverflow" in query or "stock or flow" in query:
                        speak("open   stack   overflow")
                        webbrowser.open("stackoverflow.com") 

                    elif 'open website' in query:
                        speak("Which website page should you open?")
                        source=takeCommand().lower()
                        webbrowser.open(f"https://www.google.com/search?q={source}")

#---        ------------------------------------------------------------------------
#---        ------------------- SOME OS COMMENT'S  ------------------------------------------
                    elif "play music" in query or "play song" in query  or "music" in query or  "song" in query:
                        musicdir="C:\\Users\JACKSON KASI\Music"
                        song = os.listdir(musicdir)
                        speak(" play song enjoi!")
                        # i = random.choice(song)  
                        i = range(song)
                        os.startfile(os.path.join(musicdir,i))
                        speak("sir i am exit now and i  waiting your comment")
                        break

                    elif "play video" in query :# use open cv
                        videodir="C:\\Users\\JACKSON KASI\\Videos"
                        videos=os.listdir(videodir)
                        # vid=random.choice(videos)
                        os.startfile(os.path.join(videodir,videos[0]))
#---        ------------- OPEN APP'S AND KILL APP'S [OS COMMENTS] --------------------------
                    elif "open code" in query  or "vs code" in query or "visual studio" in query:
                        speak("visual studio")
                        codepath="C:\\Users\\JACKSON KASI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codepath)
                    elif "open chrome"in query or "chrome" in query:
                        codepath1="C:\Program Files\Google\Chrome\Application\chrome.exe"
                        speak("open  chrome")
                        os.startfile(codepath1)
#---        -------------- SIMPLE WORK'S ------------------------------------------
                    elif "what is time" in query or "time" in query:
                        time=datetime.datetime.now().strftime("%H:%M")
                        print(time)
                        speak(time)
                    elif "what is date" in query or "date" in query:
                        date=time.asctime(time.localtime(time.time()))
                        print(date)
                        speak("is today is",date)
                    
                    elif "close" in query:
                        speak("sir i am exit now and i  waiting your comment")
                        exit

#---        ---------------Will try again if wrong----------            
                except Exception as e:
                        print(e)
                        speak(" please try again ")
                        continue    

        else:
            continue
