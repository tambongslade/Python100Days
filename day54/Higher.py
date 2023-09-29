from flask import Flask
import random
app = Flask(__name__)
num = random.randint(0,9)

@app.route("/")
def hello():
    return ('<h1> Guess a number between 0 and 9 </h1>'
            '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp"/>')
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > num:
        return ("<h1> too High</h1>"
                "<img src='https://media3.giphy.com/media/IsfrRWvbUdRny/200w.webp?cid=ecf05e47v8zhruqc8cahhk7m0466jtky3q9sb3g5be2e3uci&ep=v1_gifs_related&rid=200w.webp&ct=g'/>")
    if guess < num:
        return ("<h1> Too Low </h1>"
                "<img src='https://giphy.com/gifs/other-numbers-UDU4oUJIHDJgQ'/>")
    else:
        return "<img src='https://media1.giphy.com/media/Y3qaJQjDcbJPyK7kGk/200w.webp?cid=ecf05e47uokvd0g3cx4jal0d1cn4svatafs1jlqpqpmhoc4h&ep=v1_gifs_search&rid=200w.webp&ct=g'/>"
if __name__ == "__main__":
    app.run(debug=True)