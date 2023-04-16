import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

basliklar = soup.find_all("td", {"class": "titleColumn"})
ratingler = soup.find_all("td", {"class": "ratingColumn imdbRating"})

for i, j in zip(basliklar, ratingler):
    print("NAME:", i.text.replace("\n", "").replace("     ", "").strip(), "\nIMDb:", j.text.strip())
    print("--------------------")
