import requests
from bs4 import BeautifulSoup

def get_games_data():
    """Scrapes popular Steam games from store.steampowered.com (Top Sellers)."""
    url = "https://store.steampowered.com/search/?filter=topsellers"
    response = requests.get(url)
    games = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', class_='search_result_row')
        for row in results[:10]:
            title = row.find('span', class_='title').text.strip()
            price = row.find('div', class_='search_price').text.strip()
            games.append({'title': title, 'price': price})
    return games

