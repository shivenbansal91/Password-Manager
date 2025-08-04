from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    special = ['!','@','#','$','%','^','&','*','(',')']


    alpha = random.randint(8,10)
    num = random.randint(2,4)
    spec = random.randint(2,4)

    password_entry.delete(0,END)

    password_letters = [ random.choice(alphabets) for _ in range(alpha)]

    password_numbers = [random.choice(numbers) for _ in range(num)]

    password_symbols = [random.choice(special) for _ in range(spec)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)






# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password
        }
    }

    if(len(website) == 0 or len(password) == 0):
        messagebox.showinfo(title="Oops" , message= "please dont leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data , data_file , indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data , data_file , indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("data.json" , "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error" , message="No Data File Found.")
    else:
        if(website in data):
            messagebox.showinfo(title= website , message= f"Email: {data[website]["email"]} \nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error" , message= f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(row=0,column=1)

#labels

website_label = Label(text="Website: ")
website_label.grid(row=1 , column=0)


email_label = Label(text="Email/Username: ")
email_label.grid(row=2 , column=0)


password_label = Label(text="Password: ")
password_label.grid(row=3 , column=0)


#entries
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()


email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"your@gmail.com") 

password_entry = Entry(width= 22)
password_entry.grid(row=3, column=1)

#buttons

generate_password_button = Button(text="Generate Password", width=14 ,command=generate_password)
generate_password_button.grid(row=3, column=2)

add_butoon = Button(text="Add" , width=36, command=save)
add_butoon.grid(row=4, column=1, columnspan=2)

search_button = Button(text= "Search" , width=14 , command= search)
search_button.grid(row=1, column=2)





window.mainloop()