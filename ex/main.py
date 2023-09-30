from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url='https://api.npoint.io/8c31d8befba7c3dad605')
    data = response.json()
    post = data
    print(post)
    return render_template("index.html", all_post=post)
@app.route('/blog/<id>')
def blog(id):
    response = requests.get(url='https://api.npoint.io/8c31d8befba7c3dad605')
    data = response.json()[id]
    return render_template('post.html', post=data)
if __name__ == "__main__":
    app.run(debug=True)
