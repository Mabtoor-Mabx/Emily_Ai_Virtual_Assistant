# Required Libraries
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import pygame
import requests
import os
import time
from datetime import datetime

# Initialize recognizer
recognizer = sr.Recognizer()

# Speak function using gTTS and pygame
def speak(text):
    print(f"[SPEAK]: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("voice.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    os.remove("voice.mp3")

# Weather Report for Faisalabad
def get_weather_faisalabad():
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 31.418,
            "longitude": 73.0791,
            "current_weather": True
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        weather = data.get("current_weather", {})

        if weather:
            temperature = weather.get("temperature")
            windspeed = weather.get("windspeed")
            time_of_report = weather.get("time")

            report = (
                f"The current weather in Faisalabad as of {time_of_report} is "
                f"{temperature} degrees Celsius with a wind speed of {windspeed} kilometers per hour."
            )
            speak(report)
        else:
            speak("Sorry, I couldn't fetch the weather data for Faisalabad.")

    except Exception as e:
        print("[WEATHER ERROR]:", e)
        speak("There was an error getting the weather for Faisalabad.")

 #Nobel Prize Information
def get_nobel_prize_list():
    try:
        url = "http://api.nobelprize.org/2.1/laureates?sort=asc"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            laureates = data.get("laureates", [])
            # a person who is honoured with an award for outstanding creative or intellectual achievement.
            speak("Here are some of the Nobel Prize winners:")

            for laureate in laureates[:5]:  # Limit to 5 entries
                name = laureate.get("fullName", {}).get("en", "Unknown")
                born = laureate.get("birth", {}).get("date", "Unknown")
                prizes = laureate.get("nobelPrizes", [])

                for prize in prizes[:1]:  # Just first prize entry
                    year = prize.get("awardYear", "Unknown")
                    category = prize.get("category", {}).get("en", "Unknown")

                    info = f"{name}, born {born}, won the Nobel Prize in {category} in {year}."
                    speak(info)
        else:
            speak("Sorry, I couldn't fetch the Nobel Prize data.")

    except Exception as e:
        print("[NOBEL ERROR]:", e)
        speak("There was an error retrieving the Nobel Prize information.")

# Process user command
def processCommand(c):
    while True:
        print("[COMMAND]:", c)
        current_time = datetime.now().strftime("%I:%M %p on %A, %B %d")
        speak(f"The time is {current_time}")

        command = c.lower()

        if "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google. Command Executed Successfully!")
            break
        elif "open facebook" in command:
            webbrowser.open("https://facebook.com")
            speak("Opening Facebook. Command Executed Successfully!")
            break
        elif "open whatsapp" in command:
            webbrowser.open("https://web.whatsapp.com")
            speak("Opening WhatsApp. Command Executed Successfully!")
            break
        elif "news" in command:
            r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9270dbe9ca57472fb4cbf603327e0556")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles[:5]:
                    speak(article['title'])
            break
        elif "nobel prize" in command or "noble prize" in command:
            get_nobel_prize_list()
            break
        elif "weather of faisalabad" in command or "weather in faisalabad" in command:
            get_weather_faisalabad()
            break
        else:
            speak("Could you please say it again?")
            break

# Main Loop
if __name__ == "__main__":
    speak("Initializing Emily...")
    time.sleep(1)

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Emily'...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("[RECOGNIZED]:", word)

            if word.lower() == "emily":
                speak("Yes, I am listening!")
                time.sleep(1)

                with sr.Microphone() as source:
                    print("Listening for your command...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)

                c = recognizer.recognize_google(audio)
                processCommand(c)

        except sr.UnknownValueError:
            print("[ERROR]: Could not understand audio.")
        except sr.RequestError as e:
            print("[ERROR]: Recognition service error:", e)
        except Exception as e:
            print("[ERROR]:", e)
