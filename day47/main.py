import requests
from bs4 import BeautifulSoup

response = requests.get("https://1xbet.cm/allgamesentrance/crash")
soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

