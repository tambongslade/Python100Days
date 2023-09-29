from flask import Flask,render_template
import random
import datetime
import requests
app = Flask(__name__)

@app.route("/")
def home():
    random_num = random.randint(0,10)
    date = datetime.datetime.now().year
    return render_template('index.html',num=random_num,dat= date)
@app.route("/guess/<string:name>")
def guess(name):
    response = requests.get(url=f'https://api.agify.io?name={name}')
    data = response.json()
    return render_template('game.html',user=name)

@app.route("/blog")
def blog():
    blogUrl= 'https://api.npoint.io/490439da44c44cfc3e40'
    response = requests.get(url=blogUrl)
    all_post = response.json()
    return render_template('blog.html', post=all_post)
if __name__ == '__main__':
    app.run(debug=True)