import tkinter as tk
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_function():
    passwd_entry.delete(0, tk.END)
    password_list = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for char in range(nr_symbols)]
    password_list += [random.choice(symbols) for char in range(nr_numbers)]

    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password = ""
    for char in password_list:
        password += char
    passwd_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_function():
    website_data = webstie_entry.get()
    user_data = user_entry.get()
    passwd_data = passwd_entry.get()

    if website_data == "" or user_data == "" or passwd_data == "":
        messagebox.showinfo(message="Please check the inputs.")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"Email:{user_data}\nPassword:{passwd_data}")
        if is_ok:
            concatenate_data = f"{website_data} | {user_data} | {passwd_data}\n"
            with open("data.txt", mode="a") as file:
                file.write(concatenate_data)
            webstie_entry.delete(0, tk.END)
            passwd_entry.delete(0, tk.END)




# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager 1.0")
window.config(padx=20, pady=20)

image_path = "logo.png"
photo_image = tk.PhotoImage(file=image_path)
canvas = tk.Canvas(height=200, width=200)
canvas.create_image(100, 90, image=photo_image)
canvas.grid(column=1, row=0)

webstie_lable = tk.Label(text="Website: ")
webstie_lable.grid(column=0, row=1)

webstie_entry = tk.Entry(width=30)
webstie_entry.grid(column=1, row=1, columnspan=2)
webstie_entry.focus()

user_lable = tk.Label(text="Username: ")
user_lable.grid(column=0, row=2)

user_entry = tk.Entry(width=30)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "jimjimlin@gmail.com")

passwd_lable = tk.Label(text="Password: ")
passwd_lable.grid(column=0, row=3)

passwd_entry = tk.Entry(width=20)
passwd_entry.grid(column=1, row=3)

passwd_button = tk.Button(text="Generate",width=6, command=generate_function)
passwd_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=15, command=add_function)
add_button.grid(column=1, row=4)

window.mainloop()