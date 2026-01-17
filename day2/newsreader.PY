import requests


api_key = "258b1eaf9a634f6197d7fa2ff27acbfc"
news_type = "top-headlines"

url = f"https://newsapi.org/v2/{news_type}?sources=techcrunch&apiKey={api_key}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for article in articles:
    print(article["title"])
    print(article["description"])
    print("Article URL:", article["url"])
    print("\n**************************************\n")