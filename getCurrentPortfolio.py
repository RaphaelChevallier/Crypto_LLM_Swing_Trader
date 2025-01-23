from kucoin.client import User

def get_trading_account_portfolio(api_key: str, api_secret: str, api_passphrase: str) -> dict:
    """
    Retrieves the current portfolio for the Trading Account from KuCoin as a dictionary.
    
    Args:
        api_key (str): Your KuCoin API key.
        api_secret (str): Your KuCoin API secret.
        api_passphrase (str): Your KuCoin API passphrase.
        
    Returns:
        dict: A dictionary containing currency balances for the Trading Account.
    """
    try:
        # Initialize KuCoin client
        client = User(api_key, api_secret, api_passphrase)

        # Fetch all account balances
        accounts = client.get_account_list()

        # Filter accounts to only include the Trading Account
        portfolio = {}
        for account in accounts:
            if account['type'] == 'trade':  # Filter for trading account
                balance = float(account['balance'])
                if balance > 0: 
                    currency = account['currency']
                    available = float(account['available'])
                    holds = float(account['holds'])

                portfolio[currency] = {
                    'total_balance': balance,
                    'available': available,
                    'holds': holds
                }
        
        return portfolio
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}