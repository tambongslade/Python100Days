import requests
import html

question_data = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean").json()["results"]