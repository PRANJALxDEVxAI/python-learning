import requests

API_KEY = "99ce8adb6e24442cb8303b9faa1a5fc1"

topic = input("Enter topic: ")

url = f"https://newsapi.org/v2/everything?q={topic}&language=en&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)

data = response.json()

articles = data["articles"]

for i, article in enumerate(articles[:5], start=1):
    print(f"\nNews {i}")
    print("Title:", article["title"])
    print("Source:", article["source"]["name"])
    print("Published:", article["publishedAt"])
    print("Link:", article["url"])