from flask import Flask, render_template
import requests

response = requests.get('https://api.npoint.io/3a215b78bbe7de62a242').json()


app = Flask(__name__)


@app.route('/')
def get_all_post():
    return render_template('index.html', all_post=response)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
            print(requested_post)
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
