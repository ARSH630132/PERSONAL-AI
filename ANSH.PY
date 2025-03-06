import pyttsx3
import speech_recognition as sr#IMPORT SPEECH RECOGNITION IT TAKE OUR SOUND WITH THE HELP OF OUR MICROPHONE WE USE IT AS S
import datetime #TO GET THE DIRECT DATE AND TIME
import wikipedia#HERW WE IMPORT WEKIPEDIA
import webbrowser#INBUILT MODULE TO OPEN YOUTUBE ,FB ETC
import os #TO IMPORT SYSTEM THINGS LIKE MUSIC,CONTACT ETC
import random
import time#to use time function
# from pywhatsapp import WhatsAPIDriver




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') #MICROSOFT KI AUDIO PROPERTY IMPORT KRA GYA H
print(voices[1].id)#TO USE MALE VOICE OF MS WE ENTER 0 OTHERWISE ENTER 1
engine.setProperty('voice',voices[1].id)#HERE WE SELECT MS MALE VOICE
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():#CREATE A FUNCTION TO WISH 
    hour=int(datetime.datetime.now().hour)    #THIS FUNCTION SAY GOOD MORNING AND NIGHT ACCORDING TO THE TIME
    if hour >=0 and hour<12:#WE GIVE THE CONDITION OF TIME WHEN HE SAY GOOD MORNING AND GOOD AFTERNOON
        speak(" HELLO SIR GOOD MORNING !")
    elif hour>=12 and hour<=18:
        speak("HELLO SIR GOOD AFTERNOON !")  
    else:
        speak(" HELLO SIR GOOD EVENING !")
    speak("I AM ansh YOUR PERSONAL VOICE ASSISTANT HOW MAY I HELP YOU SIR")      #THIS LINE ALWAYS SPEAK BY MARK(AI NAME)    
def takecommand(): #THIS FUNCTION TAKE THE COMMAND FROM USER
    r=sr.Recognizer()#THIS TAKE OUR COMMAND WITH THE HELP OF OUR MICROPHONE   
    with sr.Microphone(1) as source:#HERE WE GIVE THE ACCESS OF OUR MICROPHONE 
        print("LISTENING YOUR  COMMAND ...") #HERE WE PRINT THIS TO SHOW IN OUTPUT NOW OUR ASSISTANT LISTEN US 
        r.pause_threshold=1 #HERE WE GIVE 3SEC TO WAIT WHEN WE SPEAK BY USING THIS WE CAN TAKE REST FOR 3 SEC IT CONTINUE ITS RECOGNITION
        audio=r.listen(source)#THIS ALL COMES FROM SPEAK MODULE WHICH IS INBUILT MODULE
    try:
        print("RECOGNIZING...")  
        querry=r.recognize_google(audio,language='en-in') #THIS GOOGLE MODULE IS ALREADY INBUILT (EN-IN=INDIA ENGLISH LANGUAGE) 
        print(f"SIR SAID  : {querry}\n")
    except Exception as e:#IF AN ERROR OCCUR THEN THIS CODE RUN 
        speak("SORRY SIR I CAN'T RECOGNIZE PLEASE SAY THIS AGAIN") 
        return"None" 
    return querry
if __name__ == "__main__":
    speak("")#CALL THE SPEAK FUNCTION (LINE NO .7)
    wishme()#CALL THE FUNCTION WHERE WE SELECT DATE AND TIME  (LINE NO.11)
    while True:
        
        querry=takecommand().lower()#HERE WE CALL TAKECOMMAND FUNCTIOIN FROM LINE(20)
        if 'wikipedia' in querry:
            speak('searching wekipedia..')#WIKIPEDIA SE JO AAYEGA WO BOLEGA
            querry=querry.replace("wekipedia","")
            results = wikipedia.summary(querry,sentences=2)
            speak("ACCORDING TO WIKIPEDIA")
            print(results)#GOOGLE SE JO MILEGA USKO PRINT KRDEGA
            speak(results)#YE USI RESULT KO BOLEGA
        elif 'open youtube' in querry:#HERE WE GIVE CONDITION IF WE SAY OPEN YOUTUBE THEN YOUTUBE OPEN
            speak("wait a few sec i open youtube")
            webbrowser.open("youtube.com")
            # break
        elif 'open google' in querry:#HERE WE GIVE TASK TO OPEN GOOGLE AND SO ON
            speak("wait a few sec i open google")
            webbrowser.open("google.com")
            # break
        elif 'open facebook' in querry:
            webbrowser.open("facebook.com")
            # break
        # elif 'open whatsaap' in querry:
        #     # Initialize the driver
        #     driver = WhatsAPIDriver()
        #     driver.send_message("6306113500", "Hello")
        #     driver.quit()
            
        elif 'play music' in querry:
            music_dir="C:\\Users\\arsh8\\OneDrive\\Desktop\\music"
            song=os.play(music_dir)
            # music_dir=random.randint(0,7)
            
            print(song)
            
            
           
        elif 'open video' in querry:
            video_dir="C:\\Users\\arsh8\\OneDrive\\Desktop\\Project videos"
            video=os.listdir(video_dir)
            break
        elif 'open instagram' in querry:
            speak("wait a few sec i open instagram")
            webbrowser.open("instagram.com")
            break
            
        elif 'the time' in querry:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"{time}")
            speak(f"SIR THE TIME IS {time}") 
               
        elif 'open code' in querry:
            code="C:\\Users\\arsh8\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   #set path of the file
            os.startfile(code) 
        elif' your name'in querry:
            speak("I AM ,ansh  AND I AM YOUR PERSONAL assistant ")
        elif'how are you'in querry:
            speak("i am fine     what about you ") 
        elif' fine'in querry:
            speak("that's a good news ")
        elif'my contact number' in querry:
            print("6306113500")
            speak("SIR your contact number is 6306113500")
            
        elif'shut down yourself' in querry:
            print("ok sir BUT YOU NEED ANY HELP THEN YOU CAN CALL ME   THANKYOU SIR HAVE A GOOD DAY")
            speak("ok sir BUT YOU NEED ANY HELP THEN YOU CAN CALL ME .THANKYOU SIR HAVE A GOOD DAY")
            break           
        elif'date' in querry:
            t=time.strftime("%d/%m/%y and time is %H:%M:%S")#to print the current date and time
            print(t)
            speak(t)
        elif"contact" in querry:
            dict={"Papa":7355552080,"Aakriti":6386955248,"Sandeep bhaiya":8382000479,"Deepak bhaiya":7380475392,"Prince":7525993819,"Bade papa":9794435680,"Badi mummy":9794433623,"Dadi":7380976726,"Rohit":6387222026,"Akhilesh":9555451785,"Roshan":9616657351,"Aryan":7355384705,"Rohan":8423712322,"Ritika":9795032440,"Arsh":6306113500,"Ankit":9569938191,"Awadhesh":7518881822}
            c="TELL THE NAME OF A PERSON WHO'S CONTACT NUMBER YOU WANT : "
            speak(c)
            print(c)
            d=str(takecommand()) #THIS TAKE OUR COMMAND WITH THE HELP OF OUR MICROPHONE
            e="CONTACT NUMBER OF ",d,"is", dict[d]
            print(e)
            speak(e)
        elif"thank" in querry:
            c="MOST WELCOME HAVE A GOOD DAY "
            print(c)
            speak(c)
        elif"take rest" in querry:
            
            print("OK I AM GOING TO SLEEP FOR 1 MIN ")
            speak("OK I AM GOING TO SLEEP FOR 1 MIN ")
            time.sleep(60)
        
            
        

            
