''' project Name----> AI Assistant
    description of project: Our AI Assistant greets at the start of the application, tells time, performs google search, find things on wikipedia and prints the 
    output in the terminal,opens stackoverflow and youtube,hear jokes, we can also store notes in a file (notes are input and stored in file) and can also hear the stored notes
    using our AI Assistant. We can change the voices from male to female and vice versa'''

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os # interactions with os
import pyjokes 


engine = pyttsx3.init('sapi5')   #text to speech (pyttsx3) {sapi5 for win, nsss for mac}
voices = engine.getProperty('voices') # voices attribute created now we can change the voices 
engine.setProperty('voice', voices[2].id) #voices[0]--male voice ,voices[1]--female voice
engine.setProperty('volume',1.0) # can lower voice vol from 0 to 1
engine.setProperty('rate',200) # controlling how fast the AI assistant should speak

# converts the text into voice 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    ''' calculate current time and on the basis of time greets the user.
    12:00 am to 11.59 am ---->good morning
    12.00 pm to 5:59 pm ---->good afternoon
    otherwise good evening '''

    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am ur AI Assistant. Please tell me how may I help you")       



def takeCommand():
    '''It takes microphone input from the user and returns string output
    now the audio is passed into the variable query which will be used to perform actions'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        '''eg. we say wikipedia laptop : the query will be wikipedia and then it searches for laptop and returns 2 sentences about laptop in audio and text'''
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # opens youtube in default browser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        # opens google in default browser
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        # opens stackoverflow in default browser
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        # plays music present in the directory
        elif 'play music' in query:
            music_dir = 'D:\\Downloads\\music\\'   # please enter a path for the audio present locally in ur computer
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        # tells time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        # we can dictate notes as note my name is AI Assistant...it stores my name is Ai assistant in the note.txt
        elif 'note' in query:
            speak("Taking notes")
            query=query.replace('note',"")
            f=open("note.txt","a")
            f.write(query)
            f.close()

        # we can open the notes we have stored...show and our ai assistant will dictate the contents present in the file
        elif 'show' in query:
            f=open("note.txt","r")
            speak(f.read())

        # tells us a joke
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        
        elif 'change voice to male' in query:
            engine.setProperty('voice', voices[0].id)
            speak('voice has been changed')


        elif 'change voice to male' in query:
            engine.setProperty('voice', voices[1].id)
            speak('voice has been changed')


           
