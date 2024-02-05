
## Active development and improvements are underway. Your feedback and contributions are welcome!
# MLTrader Bot

MLTrader Bot is a sophisticated trading bot designed to automate stock trading decisions based on market news sentiment analysis. Utilizing the Alpaca API for trading and market data, the bot performs sentiment analysis on recent news articles to make buy or sell decisions. This README outlines the bot's functionality, setup instructions, and usage.

## Features

- **Automated Trading**: Leverages the Alpaca API to execute buy and sell orders based on sentiment analysis.
- **Market News Sentiment Analysis**: Uses FinBERT, a pre-trained natural language processing model, to estimate the sentiment of market news.
- **Risk Management**: Calculates position sizing based on the user-defined percentage of cash at risk.
- **Backtesting**: Includes functionality for backtesting the strategy using historical data from Yahoo Finance.

## Prerequisites

Before you can run MLTrader Bot, you need to have the following installed:
- Python 3.6 or later
- `dotenv` for loading environment variables
- Alpaca trade API
- `lumibot` framework for trading strategies
- `finbert` for sentiment analysis

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Install the required Python packages using `pip`:
   ```
   pip install python-dotenv alpaca-trade-api lumibot finbert-utils
   ```

3. **Configure API Keys**: Sign up for an Alpaca account and obtain your API key and secret. Create a `.env` file in the root of the project and add your API keys:
   ```
   API_KEY='your_api_key'
   API_SECRET='your_api_secret'
   ```

4. **Adjust Configuration**: Modify the `MLTrader` class parameters in the script to suit your trading preferences, such as `symbol` and `cash_at_risk`.

## Usage

To run the bot, execute the script from your terminal:
```
python path/to/your_script.py
```

By default, the bot performs a backtest using historical data. To switch to live trading, uncomment the relevant sections in the script and ensure you are using a funded Alpaca account.

## How It Works

1. **Initialization**: The bot initializes with specified trading symbols and risk parameters.
2. **Sentiment Analysis**: It retrieves recent news articles for the given symbol and performs sentiment analysis.
3. **Trading Decision**: Based on the sentiment analysis outcome, the bot decides whether to buy, sell, or hold.
4. **Order Execution**: Executes buy or sell orders through the Alpaca API with calculated position sizes and risk management strategies.

## Disclaimer

This bot is for educational and research purposes only. Please do your due diligence before using it for live trading. The creators are not responsible for any financial loss incurred using this bot.

## Contributions

Contributions are welcome. Please submit a pull request or open an issue for any bugs or feature requests.
