import requests

api_address = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ffbe1733cc254d56b06548b0ea470f0a"

json_data = requests.get(api_address).json()

ar = []
news_fetched=False

def news():
    global ar, news_fetched
    if news_fetched:
        return ar

    try:
        for i in range(3):
            title = json_data["articles"][i]["title"]
            ar.append(f"Number {i + 1}: {title}.")
        news_fetched = True
        return ar
    except KeyError:
        return ["Error: Could not fetch the articles. Please check the API response."]
    except IndexError:
        return ["Error: Less than 3 articles available in the response."]
arr = news()

arr_again=news()
