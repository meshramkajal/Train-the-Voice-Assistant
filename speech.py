import speech_recognition as sr
import pyttsx3
import pandas as pd
import webbrowser  # Import the webbrowser module

# Load CSV data
data = pd.read_csv('website_summary (1).csv')

# Initialize speech recognition
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        # Recognize user's speech
        user_input = r.recognize_google(audio)
        print("User said:", user_input)

        # Process user input and provide responses based on CSV data
        if user_input in data['Page Name'].values:
            summary = data[data['Page Name'] == user_input]['Summary'].values[0]
            url = data[data['Page Name'] == user_input]['URL'].values[0]

            print("URL:", url)
            print("Summary:", summary)

            if url.startswith('http://') or url.startswith('https://'):
        # Open the URL in a web browser
                webbrowser.open(url)
            else:
                print("Invalid URL:", url)

            # Convert and play the summary as speech
            engine.say(summary)
            engine.runAndWait()
        else:
            print("Page not found. Available pages:")
            print(data['Page Name'].values)  # Print available page names

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
