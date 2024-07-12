import requests
import config

def make_call(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

    querystring = {"symbol":ticker,"region":"US"}

    headers = {
        "X-RapidAPI-Key": config.getConfig("api_key"),
        "X-RapidAPI-Host": config.getConfig("api_host")
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    if response != {}:
        price = response["summaryDetail"]["ask"]["fmt"]
        return price
    else:
        return "NOT FOUND"
    

def utils_get_news(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"
    querystring = {"q":ticker,"region":"US"}

    headers = {
        "X-RapidAPI-Key": config.getConfig("api_key"),
        "X-RapidAPI-Host": config.getConfig("api_host")
    }

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    if response != {}:
        articles = response["news"]
        news = f"The news for {ticker}:\n"
        for page in articles:
            news += page["title"]
            news += "\n"
            news += page["link"]
            news += "\n"
        return news
    else:
        return "NOT FOUND"