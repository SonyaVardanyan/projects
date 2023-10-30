#!/usr/bin/python3
import speech_recognition as sr
import os

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

# Function to recognize and process voice commands
def process_command(command):
    if "open firefox" in command:
        os.system("firefox")  
    elif "close" in command:
        os.system(f"killall -9 firefox")
    else:
        print("Command not recognized")

# Function to capture audio and recognize speech
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        process_command(command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "main":
    while True:
        listen_for_command()