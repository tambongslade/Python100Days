import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "13Q11RNLEKMSV5Q1"
STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}.LON&outputsize=full&apikey={STOCK_API_KEY}"
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey=dbbcaf69251143c091c9237b77335eb2"
NEWS_API = "dbbcaf69251143c091c9237b77335eb2"
Sid= "AC7775d7fcc9da8c2191415fd066b1b442"
Auth_token = "52a966b01209af2c652d967dbdeaeee1"
twi = "+12568294291"
my_num = "+237670527426"
today = datetime.date.fromisoformat('2023-09-13')
yesterday = (today - datetime.timedelta(days=1))
Before_yesterday = (yesterday - datetime.timedelta(days=1))
Before_yesterday = Before_yesterday.isoformat()

yesterday_str = yesterday.isoformat()
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_ENDPOINT)
data = response.json()["Time Series (Daily)"]
print(data)
data_list = [value for (key, value) in data.items()]
yesterday_price = data_list[0]
yesterday_Closing = yesterday_price["4. close"]

Before_yesterday_price = data_list[1]
Before_yesterday_price = Before_yesterday_price["4. close"]

difference = float(yesterday_Closing) - float(Before_yesterday_price)
up_down =None
if difference>0:
    up_down ="⬆️"
else:
    up_down = "⬇️"
print(difference)
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = difference / float(yesterday_Closing) * 100
print(percentage)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage) > 5:
    news_params = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME
    }

    response = requests.get(url=NEWS_ENDPOINT,params=news_params)

    articles = response.json()["articles"]
    three_articles = articles[:3]
    formatted = [f"{STOCK_NAME}: {up_down}{difference}\n Headline: {articles['title']}. \nBrief: {articles['description']}" for article in three_articles]
    from twilio.rest import Client

    client =  Client(Sid ,Auth_token)
# Optional TODO: Format the message like this:
    for article in formatted:
        message = client.messages.create(
            body=article,
            from_=twi,
            to= my_num
        )
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
