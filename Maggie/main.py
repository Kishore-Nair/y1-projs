import webbrowser
#import os
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
            speak("Sorry, I did not understand what you said. Please try again.")
            return None
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")
            return None


if __name__ == "__main__":
    speak('hey!...whats up?')
    while True:
        print("listening...")
        query = takecommand()

        if "bye maggi" in query.lower():
            speak("goodbye!")
            exit()


        #AI mode
        if "Invoke Lama".lower() in query.lower():
            speak("Llama activated! How may I help you?")
            while True:
                print("llama listening...")
                query = takecommand()
                if  "exit lama" in query:
                    speak(handle_convo("bye"))
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

        import re
        if re.search(r'\bsearch\b', query, re.IGNORECASE) and re.search(r'\bgoogle\b', query, re.IGNORECASE):
            search_term = query.split("search")[-1].strip().replace("on google", "").replace("in google", "").strip()
            if search_term:
                speak(f"Sure! Searching for {search_term} on Google.")
                webbrowser.open(f"https://www.google.com/search?q={search_term}")
            else:
                speak("What would you like to search for?")

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
                speak(f"sure!, opening {app[0]}...")
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
        if "set a timer for" in query:
            try:
                timer_duration = int(query.split("set a timer for")[-1].split("minutes")[0].strip())
                speak(f"Timer set for {timer_duration} minutes.")
                time.sleep(timer_duration * 60)
                speak("Time's up!")
            except Exception as e:
                speak(f"Sorry, I couldn't set the timer. {str(e)}")

        #battery
        import psutil
        def check_battery():
            battery = psutil.sensors_battery()
            percent = battery.percent
            speak(f"Your battery is at {percent}%")
            if not battery.power_plugged:
                speak("Your charger is not plugged in.")
            else:
                speak("Your charger is plugged in.")


        if "battery" in query:
            check_battery()
