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

root = tk.Tk()
root.title("Simple Form")

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

root.mainloop()