import requests
from bs4 import BeautifulSoup

def get_house_data():
    """Scrapes sample housing data from divar.ir (Tehran)."""
    url = "https://divar.ir/s/tehran/apartments"
    headers = {"user-agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    houses = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ads = soup.find_all('div', class_='kt-post-card__body')
        for ad in ads[:10]:
            title = ad.find('h2')
            price = ad.find('div', {'class': 'kt-post-card__description'})
            houses.append({'title': title.text.strip() if title else "-",
                           'price': price.text.strip() if price else "-"})
    return houses

