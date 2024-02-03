from datetime import datetime, timedelta
from alpaca_trade_api import REST
from datetime import datetime
from finbert_utils import estimate_sentiment

def get_dates(get_datetime):
    today = get_datetime()
    three_days_prior = today - timedelta(days=3)
    return today.strftime('%Y-%m-%d'), three_days_prior.strftime('%Y-%m-%d')

def get_news(api, symbol, get_datetime):
    today, three_days_prior = get_dates(get_datetime)
    news_items = api.get_news(symbol=symbol, start=three_days_prior, end=today)

    news_headlines = [ev.__dict__["_raw"]["headline"] for ev in news_items]
    return news_headlines

# Example usage
api = REST(base_url="https://paper-api.alpaca.markets", key_id="PK1KCYG02ESR3FYF2WDK", secret_key="J44KTg6jzYNvOozVAhZTcs1PocZ3Nk4Rli9c8NmU")
symbol = "SPY"

# Define a function for getting the current datetime
def current_datetime():
    return datetime(2023,12,15)

# Get and display the news
news_list = get_news(api, symbol, current_datetime)
print(news_list)

print(current_datetime())
#start_date = datetime(2024,1,10)
#print(start_date)

def get_sentiment(news_list):
    probability, sentiment = estimate_sentiment(news_list)
    return probability , sentiment

#for news in news_list:
#    print(news)
#    print(estimate_sentiment(news))




