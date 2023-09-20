from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text

soup= BeautifulSoup(yc_page,"html.parser")
title = [one.getText() for one in soup.select(selector=".titleline a ")]
print(title)
score = [ele.getText() for ele in soup.find_all(name="span" , class_="score")]
print(score)
score = [int(sc.split(' ')[0]) for sc in score]
print(score)