import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
APIKEY = "ZUUPNI5KQ09BVIS1"

parameters = {
    "apikey": APIKEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
}

url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=parameters)
time_series = r.json()["Time Series (Daily)"]

    
today = datetime.today().date()
yesterday = (today - timedelta(1)).strftime('%Y-%m-%d')
day_before_yesterday = (today - timedelta(2)).strftime('%Y-%m-%d')

today_price = float(time_series[str(today)]["4. close"])
yesterday_price = float(time_series[yesterday]["4. close"])

if today_price > yesterday_price*1.05 or today_price < yesterday_price*0.95:
    print("value has changed drastically...")
print(today_price, yesterday_price)
# if yesterday in time_series and day_before_yesterday in time_series:
#     yesterday_price = time_series[yesterday]["close"]
#     day_before_yesterday = time_series[day_before_yesterday]["close"]
    





## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

