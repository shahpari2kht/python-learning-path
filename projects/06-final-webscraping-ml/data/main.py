from scraper.covid_scraper import get_covid_data
from scraper.bitcoin_scraper import get_bitcoin_price
from scraper.games_scraper import get_games_data
from scraper.house_scraper import get_house_data
from analysis.ml_predictor import predict_covid_deaths
from utils.helpers import save_to_csv

def main():
    covid_data = get_covid_data()
    save_to_csv(covid_data, 'data/covid.csv')
    print("نمونه آمار کرونا:", covid_data[:2])

    bitcoin = get_bitcoin_price()
    print("قیمت بیت‌کوین:", bitcoin)

    games = get_games_data()
    save_to_csv(games, 'data/games.csv')
    print("نمونه بازی:", games[:2])

    houses = get_house_data()
    save_to_csv(houses, 'data/houses.csv')
    print("نمونه مسکن:", houses[:2])

    predict_covid_deaths('data/covid.csv')

if __name__ == "__main__":
    main()

