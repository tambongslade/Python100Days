from flask import Flask,render_template
import requests

response = requests.get('https://api.npoint.io/3a215b78bbe7de62a242').json()

app = Flask(__name__)

@app.route('/')
def get_all_post():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)