import requests
from bs4 import BeautifulSoup

def get_bitcoin_price():
    """Scrapes and returns current Bitcoin price from coinmarketcap."""
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find('div', class_='priceValue')
        if price:
            return price.text
    return "Failed to get Bitcoin price"

