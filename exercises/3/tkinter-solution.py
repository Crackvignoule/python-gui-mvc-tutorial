import tkinter as tk

def on_click(event):
    """
    Handles button click events.
    """
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def on_key(event):
    """
    Handles key press events.
    """
    if event.keysym in '0123456789+-*/':
        return
    elif event.keysym == 'Return':
        mock_event = type(
            'Event', (object,), {'widget': tk.Button(root, text="=")}
        )()
        on_click(mock_event)
    elif event.keysym == 'Escape':
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4)
entry.focus_set()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

ROW_VAL = 1
COL_VAL = 0

for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 20", padx=20, pady=20)
    btn.grid(row=ROW_VAL, column=COL_VAL)
    btn.bind("<Button-1>", on_click)
    COL_VAL += 1
    if COL_VAL > 3:
        COL_VAL = 0
        ROW_VAL += 1

root.bind('<Key>', on_key)

root.mainloop()