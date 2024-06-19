import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
#stock api key
APIKEY = "ZUUPNI5KQ09BVIS1"
#news api key
newsAPI = "aadf084dcc73405e80648b9175777c1f"

parameters = {
    "apikey": APIKEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
}

news_parameters = {
    "q": (COMPANY_NAME),
    "from": 2024-6-19,
    "apiKey": newsAPI,

}

stock_url = 'https://www.alphavantage.co/query'
news_url = ('https://newsapi.org/v2/everything')
       
r = requests.get(stock_url, params=parameters)
time_series = r.json()["Time Series (Daily)"]
ts_sorted = sorted(time_series)
    
# today = datetime.today().date()
# yesterday = (today - timedelta(1)).strftime('%Y-%m-%d')
# day_before_yesterday = (today - timedelta(2)).strftime('%Y-%m-%d')


# today_price = float(ts_sorted[0]["4. close"])
# yesterday_price = float(ts_sorted[1]["4. close"])

#if today_price > yesterday_price*1.05 or today_price < yesterday_price*0.95:
    
response = requests.get(news_url, params=news_parameters)
data = response.json()
print(data)



# if yesterday in time_series and day_before_yesterday in time_series:
#     yesterday_price = time_series[yesterday]["close"]
#     day_before_yesterday = time_series[day_before_yesterday]["close"]
    






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

