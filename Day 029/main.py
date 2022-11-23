from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_l = [random.choice(letters) for _ in range(nr_letters)]
    password_s = [random.choice(symbols) for _ in range(nr_symbols)]
    password_n = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_l + password_s + password_n

    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    #
    # for char in password_list:
    #   password += char
    #
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_date():
    website = input_website.get()
    email = input_email.get()
    pw = input_pw.get()

    if len(website) == 0 or len(email) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{website} Password!",
                                       message=f"You entered:\nEmail: {email}\nPassword: {pw}\nIs "
                                               f"it okay to save these details?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"Website: {website}\t|\tEmail/Username: {email}\t|\tPassword: {pw}\n")

            input_website.delete(0, END)
            input_website.focus()
            # input_email.delete(0, END)
            input_pw.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

# Canvas

img_png = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_png)
canvas.grid(column=1, row=0)

# Label

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_website.focus()

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_pw = Label(text="Password:")
label_pw.grid(column=0, row=3)

# Input

input_website = Entry(width=59)
input_website.grid(column=1, row=1, columnspan=2)

input_email = Entry(width=59)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, string="sample.sample@email.com")

input_pw = Entry(width=34)
input_pw.grid(column=1, row=3)

# Button

button_generate = Button(text="Generate Password", width=20, highlightthickness=0, command=generate_pw)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=50, highlightthickness=0, command=save_date)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
