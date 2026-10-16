from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    website_data = web_entry.get().title()

    try:
        with open("data.json","r") as file:
            data = json.load(file)

    except (FileNotFoundError,json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if website_data in data:
            messagebox.showinfo(title=website_data,message=f"Email:{data[website_data]['email']}\nPassword:{data[website_data]['password']}")
        else:
            messagebox.showinfo(title="Error",message="No details found in file")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  letters_list = [choice(letters) for _ in range(randint(8, 10))]
  symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
  numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = []
  password_list.extend(letters_list + symbols_list + numbers_list)


  shuffle(password_list)

  password = "".join(password_list)

  pass_entry.insert(0,password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = web_entry.get().title()
    email_data = email_entry.get()
    pass_data = pass_entry.get()
    new_data = {
        website_data: {
            "email":email_data,
            "password":pass_data,
        }
    }

    #Message Box

    if len(website_data) != 0 and len(pass_data) != 0:
        try:
            with open("data.json","r") as file:
                #Reading old data
                data = json.load(file)

        except (FileNotFoundError,json.decoder.JSONDecodeError):
            with open("data.json","w") as file:
                json.dump(new_data,file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json","w") as file:
                #Saving updated data
                json.dump(data,file, indent=4)


        web_entry.delete(0,END)
        pass_entry.delete(0,END)
    else:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0,row=3)


#Buttons
pass_button = Button(text="Generate Password",command=generate_pass)
pass_button.grid(column=2,row=3,sticky="w")
add_button = Button(text="Add",width=44,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="w")
search_button = Button(text="Search",width=14,command=find_password)
search_button.grid(column=2,row=1,sticky="w")

#Entries
web_entry = Entry(width=33)
web_entry.grid(row=1,column=1,columnspan=2,sticky="w")
web_entry.focus()
email_entry = Entry(width=52)
email_entry.insert(0,"youremail@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,sticky="w")
pass_entry = Entry(width=33)
pass_entry.grid(row=3,column=1,sticky="w")




canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1, row=0)









window.mainloop()




