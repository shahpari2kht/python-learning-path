import requests
from bs4 import BeautifulSoup

def get_covid_data():
    """Scrapes top 10 countries' covid stats."""
    url = 'https://www.worldometers.info/coronavirus/'
    response = requests.get(url)
    data = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', id='main_table_countries_today')
        rows = table.tbody.find_all("tr") if table else []
        for row in rows[:10]:
            cols = row.find_all("td")
            if len(cols) >= 5:
                country = cols[1].text.strip()
                cases = cols[2].text.strip().replace(',', '').replace('N/A','0')
                deaths = cols[4].text.strip().replace(',', '').replace('N/A','0')
                data.append({
                    'country': country,
                    'cases': int(cases) if cases.isdigit() else 0,
                    'deaths': int(deaths) if deaths.isdigit() else 0,
                })
    return data

