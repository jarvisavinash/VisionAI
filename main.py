import speech_recognition as sr
import os
import random
import webbrowser
import datetime
import openai
from config import apikey
from pywizlight import wizlight, PilotBuilder, discovery


def say(text):
    os.system(f"say {text}")


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Todo: Wrap this inside of a  try catch block
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"prompt- {random.randint(1, 100)}", "w") as f:
        f.write(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
            print(f"command: {query}")
            return query
        except Exception as e:
            return "Analysis Mode. Password 80085"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Jarvis 1.0')
    say("Hello, I am Jarvis AI")

    while True:
        print("Listening...")
        command = takeCommand()

        sites = [["google", "https://www.google.co.in"], ["youtube", "https://www.youtube.com"],
                 ["wikipedia", "https//www.wikipedia.com"]]

        for site in sites:
            # Todo: Add more sites
            if f"Open {site[0]}".lower() in command.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

            # Todo: Add a feature to play a specific song
            elif "open music" in command:
                musicPath = "/Users/jarvis/Music/Metro-Boomin-Am-I-Dreaming.mp3"
                os.system(f"open {musicPath}")

            elif "datetime" in command:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the datetime is {strfTime}")
            elif "find bulb" in command:
                bulbs = discovery.discover_lights(broadcast_space="192.168.0.1")
                print(bulbs)

            elif "jarvis".lower() in command.lower():
                ai(prompt=command)

            elif "exit" in command.lower():
                exit()


