from tkinter import *

window = Tk()
window.title("Km Calculator")
window.config(pady=20,padx=20)

input= Entry(width=10)

input.grid(column=1,row=0)

txt= Label(text="miles")
txt.grid(column=2,row=0)
txt.config(padx=20,pady=5)

txt= Label(text="Is equal to")
txt.grid(row=1,column=0)
txt.config(padx=20,pady=5)

km = Label(text="0")
km.grid(column=1,row=1)

txt= Label(text="kM")
txt.grid(column=2,row=1)
def calculate():
    userInput=input.get()
    userInput=int(userInput)*1.6
    km.config(text=int(userInput))
button= Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)

window.mainloop()
