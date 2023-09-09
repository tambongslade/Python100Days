from tkinter import *
windows = Tk()
windows.title("My first Gui")
windows.minsize(width=500, height=300)
windows.config(padx=100,pady=200)

#label
my_label = Label(text="i am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0,column=0)


def button_clicked():
    text = input.get()
    my_label["text"] = text
    print(text)
button = Button(text="Click ME",command=button_clicked)
button.grid(row=1,column=1)
btn = Button(text="new button")
btn.grid(row=0,column=3)

input = Entry(width=30)
input.grid(row=2,column=4)





windows.mainloop()