from tkinter import *

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

website_entry = Entry(width=35, fg="gray")
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
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

password_entry = Entry(width=21, fg="gray")
password_entry.grid(row=3, column=1, sticky="EW")
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

#___________________________BUTTONS___________________________________________

generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")
#______________________________END______________________________________________

window.mainloop()