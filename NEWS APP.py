import requests
def get_news(topic):
    API_KEY = "YOUR_API_KEYPLZ"
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    response= requests.get(url)
    data = response.json()
    if data["status"] != "ok" :
        print("Error:" , data.get("message"))
        return
    
    print(f"\nLatest News on {topic}\n")

    for i ,article in enumerate(data["articles"], 1):
        print(f"{i}. {article['title']}")
        print(article["description"])
        print(article["url"])
        print("-"*50)
        

topic = input("Topic: ")
get_news(topic)
