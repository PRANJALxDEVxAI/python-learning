import requests
import pyttsx3

# ----------------- Text-to-Speech Setup -----------------
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)   # Change to voices[1] if you want another installed voice
engine.setProperty("rate", 200)
engine.setProperty("volume", 1.0)


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


# ----------------- News Function -----------------
def get_news(topic):
    API_KEY = "99ce8adb6e24442cb8303b9faa1a5fc1"

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}"
        f"&language=en"
        f"&sortBy=publishedAt"
        f"&pageSize=5"
        f"&apiKey={API_KEY}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["status"] != "ok":
            speak("Sorry, I couldn't fetch the news.")
            return

        articles = data["articles"]

        if not articles:
            speak(f"Sorry, I couldn't find any news about {topic}.")
            return

        speak(f"Here are the latest news headlines about {topic}.")

        for i, article in enumerate(articles, start=1):
            title = article.get("title", "No title available")
            description = article.get("description", "")
            content = article.get("content", "")
            source = article["source"]["name"]
            speak(title)
            print(f"\n{i}. {title}")
            speak(f"Headline {i}")
            if description:
                speak(description)

            if content:
                content = content.split("[+")[0]   # Remove the "[+1234 chars]" part
                speak(content)

            print(f"Source: {source}")
            print("-" * 60)


        speak("That's all for now.")

    except Exception as e:
        print(e)
        speak("An error occurred while fetching the news.")


# ----------------- Main Program -----------------
if __name__ == "__main__":
    topic = input("Enter news topic: ")
    get_news(topic)

    engine.stop()