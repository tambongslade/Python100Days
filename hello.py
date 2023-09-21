from flask import Flask
import random

app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
