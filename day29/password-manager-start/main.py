from tkinter import *
from tkinter import messagebox
import pyperclip
import  json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    import random
    pass_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    web = web_input.get()
    email = email_input.get()
    passd = pass_input.get()
    new_data = {
        web: {
            "email": email,
            "password": passd,
        }
    }
    if len(web) == 0 or len(passd) == 0:
        messagebox.showerror(title="NOt complete", message="Please fill out the spaces")
    else:
        try:
            with open("password.json", mode="r") as data_file:
                data= json.load(data_file)
        except FileNotFoundError:
            with open("password.json","w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            data.update(new_data)
            with open("password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_input.delete(0, END)

            pass_input.delete(0, END)
# ---------------------------- Find PAssword------------------------------- #
def Find_password():
    website= web_input.get()
    try:
        with open("password.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="file not found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)
# --------------Labels---------------
website = Label(text="Website: ")
website.grid(column=0, row=1)

email = Label(text="Email/Username : ")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)
# -------------inputs----------------
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=1)
web_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=1)
email_input.insert(0, "TambongSlade17@gmail.com")
pass_input = Entry(width=35)
pass_input.grid(column=1, row=3)

# ---------------Buttons-------------
gen = Button(text="Generate Password", width=20, command=generatePassword)
gen.grid(column=2, row=3, )
add = Button(text="Add", width=36, command=savePassword)
add.grid(column=1, row=4)
search = Button(text="Search", width=20,command=Find_password)
search.grid(column=2, row=1)

window.mainloop()
