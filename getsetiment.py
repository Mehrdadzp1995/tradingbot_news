from dotenv import load_dotenv
import os

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


load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY":API_KEY, 
    "API_SECRET": API_SECRET, 
    "PAPER": True
}



# Example usage
api = REST(base_url=BASE_URL, key_id=API_KEY, secret_key=API_SECRET)
symbol = "SPY"

# Define a function for getting the current datetime
def current_datetime():
    #return datetime(2024,2,4)
    ## Returns the current local datetime
    return datetime.now()
print(current_datetime())

# Get and display the news
news_list = get_news(api, symbol, current_datetime)
#print(news_list)

def get_sentiment(news_list):
    probability, sentiment = estimate_sentiment(news_list)
    return probability , sentiment

for news in news_list:
    print(news)
    print(estimate_sentiment(news))




