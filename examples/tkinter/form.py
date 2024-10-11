import tkinter as tk

def submit():
    print(f"Name: {name_entry.get()}, Age: {age_entry.get()}")

root = tk.Tk()
root.title("Simple Form")

tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Age").grid(row=1)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)

tk.Button(root, text="Submit", command=submit).grid(row=2, column=1)

root.mainloop()