import tkinter as tk
from tkinter import ttk

def submit():
    print(f"Name: {name_entry.get()}, Age: {age_entry.get()}")

root = tk.Tk()
root.title("Simple Form with ttk")

ttk.Label(root, text="Name").grid(row=0)
ttk.Label(root, text="Age").grid(row=1)

name_entry = ttk.Entry(root)
age_entry = ttk.Entry(root)

name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)

ttk.Button(root, text="Submit", command=submit).grid(row=2, column=1)

root.mainloop()