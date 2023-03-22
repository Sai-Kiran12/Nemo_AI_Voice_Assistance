import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import datetime
from playsound import playsound
import keyboard
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Tk
from pytube import YouTube
import pyjokes
from googletrans import Translator
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
from bs4 import BeautifulSoup
import winshell
import pyautogui
import operator
import glob



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        # window = tk.Tk()
        # greeting = tk.Label(text="Listening...")
        # greeting.pack()
        Speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        Speak("Good Afternoon Sir !")  
  
    else:
        Speak("Good Evening Sir !") 
  

    time = datetime.datetime.now().strftime('%I:%M %p')
    Speak("it's " + time)

    Speak("I am Nemo your Assistant")

    Speak("How may I help you")
wishMe()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        # window = tk.Tk()
        # greeting = tk.Label(text="Listening...")
        # greeting.pack()
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    # window.mainloop()
    
    return query.lower()



def TaskExe():

        

    def Music():
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()

        pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def video():
        Speak("Tell Me The NamE oF The Video!")
        musicName = takecommand()

        pywhatkit.playonyt(musicName)

        Speak("Your Video Has Been Started! , Enjoy Sir!")

    def GoogleMaps(Place):

        try:
            Url_Place = "https://www.google.com/maps/place/" + str(Place)

            geolocator = Nominatim(user_agent="myGeocoder")

            location = geolocator.geocode(Place , addressdetails= True)

            target_latlon = location.latitude , location.longitude

            webbrowser.open(url=Url_Place)

            location = location.raw['address']

            target = {'city' : location.get('city',''),
                        'state' : location.get('state',''),
                        'country' : location.get('country','')}

            current_loca = geocoder.ip('me')

            current_latlon = current_loca.latlng

            distance = str(great_circle(current_latlon,target_latlon))
            distance = str(distance.split(' ',1)[0])
            distance = round(float(distance),2)


            Speak(target)
            Speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

        except:
            Speak("Can you please repeat sir")

    def Songs():
        Speak("OK sir your song in playing")

        if 'play songs' in query:
            music_dir = 'C:\\Users\\ASUSVivoBOOK\\OneDrive\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play romantic songs' in query or 'play love songs' in query:
            music_dir = 'C:\\Users\\ASUSVivoBOOK\\OneDrive\\Desktop\\music1\\romantic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play sad songs' in query or 'play lonely songs' in query:
            music_dir = 'C:\\Users\\ASUSVivoBOOK\\OneDrive\\Desktop\\music1\\sad'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play random songs' in query or 'play any songs' in query:
            music_dir = 'C:\\Users\\ASUSVivoBOOK\\OneDrive\\Desktop\\music1\\random'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play happy songs' in query or 'play energetic songs' in query:
            music_dir = 'C:\\Users\\ASUSVivoBOOK\\OneDrive\\Desktop\\music1\\happy'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif ' play kpop' in query or 'play BTS songs' in query:
            music_dir = 'C:\\Users\\ASUSVivoBOOK\\OneDrive\\Desktop\\music1\\kpop'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

    # def create_playlist(path):
    #             for song in glob.glob(path):
    #                 print("Playing...",song)
    #                 playsound(song)
    
    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("C:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

        elif 'spotify' in query:
            os.startfile("C:\\Users\\ASUSVivoBOOK\\AppData\\Local\\Microsoft\\WindowsApps\\spotify.exe")

        elif 'ms word' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe")

        elif 'powerpoint' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\powerpnt.exe")

        elif 'excel' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'gmail' in query or 'mail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")


    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'spotify' in query:
            os.system("TASKKILL /F /im spotify.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('k')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

        
    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    
    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hey")
            Speak("You need any help")

        elif 'how are you' in query:
            Speak("I am fine, Thank you")
            Speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            Speak("It's good to know that your fine")

        elif 'who i am' in query or "who am i" in query:
            Speak("If you talk then definitely your human.")

        elif 'is love' in query:
            Speak("It is 7th sense that destroy all other senses")

        elif 'what is your name' in query:
            Speak('My name is Nemo')
            Speak('Your AI assistant')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            Speak("Recycle Bin Recycled")


        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            break

        elif 'exit' in query:
            Speak("OK Sir")
            break

        elif 'stop' in query:
            Speak("OK Sir")
            break

        elif 'youtube search' in query:
            Speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("yt search","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'search wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("search wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'wikipedia search' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("wikipedia search","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open spotify' in query:
            OpenApps()
        
        elif 'open gmail' in query or 'check my mail' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open ms word' in query:
            OpenApps()
        
        elif 'open powerpoint' in query:
            OpenApps()

        elif 'open excel' in query:
            OpenApps()

        elif 'close youtube' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'play video' in query:
            video()
        

        elif 'play' in query:
            Songs()

        elif 'close spotify' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'close chrome' in query:
            CloseAPPS()

        
        elif 'chrome automation' in query:
            ChromeAuto()  

        elif 'youtube auto' in query:
            YoutubeAuto()

        elif 'where is' in query:
            
            Place = query.replace('where is','')
            #Place = query.replace('how far is','')
            GoogleMaps(Place)


        elif 'calculate' in query:
            try:
                query = query.replace('calculate','')
                #r = sr.Recognizer()
                #with sr.Microphone() as source:
                    #Speak("Say what you want to calculate")
                    #print('listning.......')
                    #r.adjust_for_ambient_noise(source)
                    #audio = r.listen(source)
                #my_string=r.recognize_google(audio)
                #print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        '/' or 'divided by' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                    
                Speak('Your result is')
                Speak( eval_binary_expr(*(query.split())))

            except:
                Speak("I can't understand")

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/')

        elif 'alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%I:%M:%p")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            Speak("Video Downloaded")

        #elif 'translator' in query:
            #Tran()

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            Speak('Current time is ' + time)

        elif 'volume up' in query:
            pyautogui.press('volumeup')

        elif 'volume down' in query:
            pyautogui.press('volumedown')

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press('volumemute')

        elif 'write a note' in query:
            Speak("what should i write, sir!")
            noteop = takecommand()
            noteMsg = open('note.txt','w')
            noteMsg.write(noteop)
            noteMsg.close()

        elif 'take a note' in query:
            Speak("what should i write, sir!")
            noteop = takecommand()
            noteMsg = open('note.txt','w')
            noteMsg.write(noteop)
            noteMsg.close()

        elif "show note" in query:
            Speak("Showing Notes")
            file = open("note.txt", "r")
            Speak(file.read())

        elif 'remember that' in query or "remind me" in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = query.replace("remind me","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That :" + remeber.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")


TaskExe()
