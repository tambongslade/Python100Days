from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
Font1 = ("Arial", 60, "bold")
Font2 = ("Arial", 40, "italic")


# --------------Extracting data from the csv----------
import random
try:
    data = pandas.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv("data/french_words.csv")
data = data.to_dict(orient="records")


current_card={}
#-------Corret------------
def isKnown():
    data.remove(current_card)
    lol =pandas.DataFrame(data)
    lol.to_csv("data/Words_to_learn.csv",index=False)
    gen()

# -----generating random word-----
def gen():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(data)

    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(txt, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    flip_timer = window.after(3000,func=Flipcard)


def Flipcard():

    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(txt,text= current_card["English"],fill="white")
    canvas.itemconfig(canvas_image,image= backCard)

# ----------UI setup----------------------------------
window = Tk()
window.title("FlashCard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000,func=Flipcard)

# Buttonspa
my_image_right = PhotoImage(file="images/right.png")
button_right = Button(image=my_image_right, highlightthickness=0, command=isKnown)
button_right.grid(column=1, row=1, )

my_image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=my_image_wrong, highlightthickness=0, command=gen)
button_wrong.grid(column=0, row=1)

# -------------------------canvas---------
canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
backCard = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(415, 263, image=front_card)
title=canvas.create_text(400, 150, text="title", font=Font2)
txt = canvas.create_text(400, 263, text="word", font=Font1)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
gen()

window.mainloop()
