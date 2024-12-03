import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    
    if not name or not age or not email:
        messagebox.showerror("Validation Error", "Name, Age, and Email fields cannot be empty")
    else:
        print(f"Name: {name}, Age: {age}, Email: {email}")
        status_var.set("Form submitted successfully")

def quit_app():
    root.quit()

def show_about():
    messagebox.showinfo("About", "This is a simple form application")

root = tk.Tk()
root.title("Simple Form")

# Create menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=quit_app)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Create form
tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Age").grid(row=1)
tk.Label(root, text="Email").grid(row=2)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
email_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)

tk.Button(root, text="Submit", command=submit).grid(row=3, column=1)

# Create status bar
status_var = tk.StringVar()
status_var.set("Ready")
status_bar = tk.Label(root, textvariable=status_var, bd=1, anchor=tk.W)
status_bar.grid(row=4, columnspan=2, sticky=tk.W+tk.E)

root.mainloop()