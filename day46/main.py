import requests
from bs4 import BeautifulSoup
import spotipy


print("weeeh didn't have anything")
billboard_url = "https://www.billboard.com/charts/hot-100/"
user_input = input("which year do you want to travel to? Type the date in this format yyyy-mm-dd: ")
response = requests.get(f"{billboard_url}{user_input}")
soup = BeautifulSoup(response.text, "html.parser")
lol=[]
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)