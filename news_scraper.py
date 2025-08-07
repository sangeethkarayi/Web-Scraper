import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

response = requests.get(URL)
response.raise_for_status() 

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all(['h2', 'h3'])

headlines_text = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines_text:
        file.write(headline + "\n")

print("Headlines saved to 'headlines.txt'")
