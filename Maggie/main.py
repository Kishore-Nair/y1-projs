import webbrowser
import os
import speech_recognition as sr
import datetime
from feature.customvoice import speak
from feature.llama_for_Maggie import handle_convo

# def say(text):
#     os.system(f"say {text}")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio , language='en-in')
            print(f"user said:{query}\n")
            print("interpreting...")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand what you said. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None


if __name__ == "__main__":
    speak('hey!...whats up?')
    while True:
        print("listening...")
        query = takecommand()

        if "bye maggi" in query.lower():
            speak("goodbye!")
            exit()

        if "Invoke Lama".lower() in query.lower():
            speak("Llama activated! How may I help you?")
            while True:
                print("llama listening...")
                query = takecommand()
                if query == "exit lama":
                    speak("exited llama mode!")
                    break

                result = handle_convo(query)
                speak(result)

        #open sites
        sites = [
            ["YouTube", "https://youtube.com"],
            ["Google", "https://google.com"],
            ["Facebook", "https://facebook.com"],
            ["Twitter", "https://twitter.com"],
            ["Instagram", "https://instagram.com"],
            ["LinkedIn", "https://linkedin.com"],
            ["Wikipedia", "https://wikipedia.org"],
            ["Reddit", "https://reddit.com"],
            ["Amazon", "https://amazon.com"],
            ["Netflix", "https://netflix.com"],
            ["GitHub", "https://github.com"],
            ["Stack Overflow", "https://stackoverflow.com"],
            ["Pinterest", "https://pinterest.com"],
            ["TikTok", "https://tiktok.com"],
            ["Quora", "https://quora.com"]
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"opening {site[0]}...")
                webbrowser.open(site[1])

        #open apps
        import subprocess
        import sys
        apps = [
            ["music", "Music.app"],
            ["safari", "Safari.app"],
            ["mail", "Mail.app"],
            ["photos", "Photos.app"],
            ["messages", "Messages.app"],
            ["calendar", "Calendar.app"],
            ["notes", "Notes.app"],
            ["reminders", "Reminders.app"],
            ["facetime", "FaceTime.app"],
            ["contacts", "Contacts.app"],
            ["maps", "Maps.app"],
            ["preview", "Preview.app"],
            ["finder", "Finder.app"],
            ["app store", "App Store.app"],
            ["system settings", "System Settings.app"]
        ]

        for app in apps:
            if f"open {app[0].lower()}" in query.lower():
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                try:
                    subprocess.call([opener, f"/System/Applications/{app[1]}"])
                except Exception as e:
                    print(f"Failed to open {app[1]}: {e}")


        #time
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            mins = datetime.datetime.now().strftime("%M")
            speak(f"the time is {hour} hours and {mins} minutes")


