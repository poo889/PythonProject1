import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer=sr.Recognizer()
engine =pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def proccessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif   "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")



    
if __name__=="__main__":
    speak("initializing Guddi.....")
    #listen the word
    while True:
        r=sr.Recognizer() 
        print("recognizing...")   
        try:
            with sr.Microphone() as source:
                
                print("Listening...")
                audio= r.listen(source, timeout=5, phrase_time_limit=5)
                word= r.recognize_google(audio)
                if(word.lower()=="guddi"):
                    
                    speak("ya")
                    with sr.Microphone() as source:
                
                     print("guddi Active....")
                     audio= r.listen(source, timeout=2, phrase_time_limit=1)
                
                     command= r.recognize_google(audio)
                     proccessCommand(c)
        except Exception as e:
            print("Error:{0}".format(e))            
    
    