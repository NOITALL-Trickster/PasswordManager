import json
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

FONT = ("Arial", 10, "bold")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#_____________________________WEBSITE RELATED__________________________________
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=32, fg="gray")
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()
website_placeholder = "Enter your website here"
website_entry.insert(0, website_placeholder)

def on_focus_in(event):
    if website_entry.get() == website_placeholder:
        website_entry.delete(0, END)
        website_entry.config(fg="black")

def on_focus_out(event):
    if website_entry.get() == "":
        website_entry.insert(0, website_placeholder)
        website_entry.config(fg="grey")

website_entry.bind("<FocusIn>", on_focus_in)
website_entry.bind("<FocusOut>", on_focus_out)
#____________________________END______________________________________________

#_____________________________USERMAIL RELATED__________________________________
usermail_label = Label(text="Email/Username:", font=FONT)
usermail_label.grid(row=2, column=0)

usermail_entry = Entry(width=35, fg="gray")
usermail_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
usermail_placeholder = "Enter your email or username here"
usermail_entry.insert(0, usermail_placeholder)

def on_mail_in(event):
    if usermail_entry.get() == usermail_placeholder:
        usermail_entry.delete(0, END)
        usermail_entry.config(fg="black")

def on_mail_out(event):
    if usermail_entry.get() == "":
        usermail_entry.insert(0, usermail_placeholder)
        usermail_entry.config(fg="grey")

usermail_entry.bind("<FocusIn>", on_mail_in)
usermail_entry.bind("<FocusOut>", on_mail_out)

#____________________________END______________________________________________

#_____________________________PASSWORD RELATED__________________________________
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=32, fg="gray")
password_entry.grid(row=3, column=1, sticky="W")
password_placeholder = "Enter your password here"

password_entry.insert(0, password_placeholder)

def on_password_in(event):
    if password_entry.get() == password_placeholder:
        password_entry.delete(0, END)
        password_entry.config(fg="black")

def on_password_out(event):
    if password_entry.get() == "":
        password_entry.insert(0, password_placeholder)
        password_entry.config(fg="grey")

password_entry.bind("<FocusIn>", on_password_in)
password_entry.bind("<FocusOut>", on_password_out)

#____________________________END______________________________________________

def save_data():
    website = website_entry.get()
    email = usermail_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "email":email,
            "password":password,

        }

    }
    if website == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\n\nProceed??? ")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                usermail_entry.delete(0, END)
                password_entry.delete(0, END)

#------------------------------- Password Generator ----------------------------
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for i in range(randint(8, 10))]
    char_list = [choice(symbols) for i in range(randint(2, 4))]
    number_list = [choice(numbers) for i in range(randint(2, 4))]

    list_password = password_list + char_list + number_list

    shuffle(list_password)

    password = "".join(list_password)
    pyperclip.copy(password)
    password_entry.insert(0, password)
#-------------------------------End---------------------------------------------
#------------------------------- Find Password ----------------------------
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found.")
    else:
        try:
            data[website]
        except KeyError:
            messagebox.showerror("Error", "Website not found.")
        else:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(f"{website}", f"Email: {email}\nPassword: {password}")
#-------------------------------End---------------------------------------------
#___________________________BUTTONS___________________________________________

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

search_btn = Button(text="Search", command=find_password)
search_btn.grid(row=1, column=2, sticky="NSEW")

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")
#______________________________END______________________________________________


window.mainloop()