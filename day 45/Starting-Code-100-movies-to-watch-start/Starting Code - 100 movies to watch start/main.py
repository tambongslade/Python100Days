import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
movies = movies[::-1]
print(movies)
with open("movies.txt","a") as movie:
    for move in movies:
        movie.write(f"{move}\n")


