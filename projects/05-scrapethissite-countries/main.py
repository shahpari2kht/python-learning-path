import requests
from bs4 import BeautifulSoup
import csv

url = "https://scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

countries = []
for c in soup.select("div.country")[:20]:
    name = c.find("h3", class_="country-name").text.strip()
    capital = c.find("span", class_="country-capital").text.strip()
    population = c.find("span", class_="country-population").text.strip().replace(',', '')
    area = c.find("span", class_="country-area").text.strip().replace(',', '')
    countries.append([name, capital, population, area])

with open("countries.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Capital", "Population", "Area"])
    writer.writerows(countries)

print("Saved 20 countries info to countries.csv")
