from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get(url='https://api.npoint.io/3a215b78bbe7de62a242')
post = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_post=post)
@app.route('/post')
def post():
    return render_template('post.html', post=data)
if __name__ == "__main__":
    app.run(debug=True)
