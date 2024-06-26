from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(8, 10)]
    password_symbols = [choice(symbols) for _ in range(2, 4)]
    password_numbers = [choice(numbers) for _ in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        message = messagebox.askokcancel(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data (load data)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                # print(data)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def search():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            message = messagebox.showinfo(title=f"{website}", message=f"Email: {email} \n Password: {password}")
        else:
            message = messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

web_entry = Entry(width=32)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_entry = Entry(width=51)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "priya@gmail.com")

pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3)

search = Button(text="Search", command=search, width=13)
search.grid(column=2, row=1)
generate_pass = Button(text="Generate Password", command=password_generate)
generate_pass.grid(column=2, row=3)

add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()

