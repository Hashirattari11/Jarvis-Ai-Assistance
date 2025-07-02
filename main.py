import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import naat
import requests
# from openai import OpenAI

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

newapi = "1b433d35312b46258979a7413ce4acea"
# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = os.getenv(
    api_key=os.getenv ("GEMINI_API_KEY"),

    )
    # model = 
    # messages =


    completion = client.chat.completions.create(
    model="gemini/gemini-2.0-flash",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
        {"role": "user", "content": command}
    ]
    )

    return(completion.choices[0].message.content)


# Command processing function
def commandprocess(c):
    if "open google" == c.lower():
        webbrowser.open("https://google.com")
        speak("i am open the google")
    elif "open facebook" == c.lower():
        webbrowser.open("https://facebook.com")
        speak("i am open the facebook")
    elif "open youtube" == c.lower():
        webbrowser.open("https://youtube.com")
        speak("i am open the youtube")
    elif "open linkedin" == c.lower():  # fixed spelling
        webbrowser.open("https://linkedin.com")
        speak("i am open the linkdin")
    elif "open whatsapp" == c.lower():
        webbrowser.open("https://web.whatsapp.com")
        speak("i am open the whatsapp")
    elif c.lower().startswith("play"):
        songs = c.lower().split(" ")[1]
        Link = naat.music[songs]
        webbrowser.open(Link)
        speak("I am playing songs")
    elif 'news' in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles",[])
            for article in articles:
                speak(article['title'])
                speak("yes tell me news some wait")
        

    else:
        output = aiprocess(c)
        speak(output)

# Main loop
if __name__ == "__main__":
    speak("Listening, Jarvis... ")
    while True:
        r = sr.Recognizer()
        print("recognize...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("ya i am here")
                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    commandprocess(command)  # passed the 'command' argument
        except Exception as e:
            print("Error:", e)
