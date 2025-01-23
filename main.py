import pandas
import os
from dotenv import load_dotenv
from getCurrentPortfolio import get_trading_account_portfolio
import kucoin.websocket

load_dotenv()

def main():
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    API_PASSPHRASE = os.getenv('PASSPHRASE')
    portfolio = get_trading_account_portfolio(API_KEY, API_SECRET, API_PASSPHRASE)
    print(portfolio)


if __name__ == "__main__":
    main()