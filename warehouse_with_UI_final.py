import tkinter as tk
items_dict = {}
history = []


def remove(name, count):
    clear_text_widget_and_buttons()
    if name in items_dict.keys():
        if items_dict[name] < count:
            text_widget.insert(tk.END, f"Not enough quantity, we only have {items_dict[name]} {name}.")
        else:
            items_dict[name] -= count
            text_widget.insert(tk.END, f"You have removed {count} {name}.")
            history.append(f"You have removed {count} {name}.")
    else:
        text_widget.insert(tk.END, f"Sorry, we do not have any {name}.")


def load(name, count):
    clear_text_widget_and_buttons()
    if name not in items_dict.keys():
        items_dict[name] = count
    else:
        items_dict[name] += count
    text_widget.insert(tk.END, f"You have restocked {count} {name}.")
    history.append(f"You have restocked {count} {name}.")


def audit():
    clear_text_widget_and_buttons()
    text_widget.insert(tk.END, "Current stock in warehouse:\n")
    for key, value in items_dict.items():
        text_widget.insert(tk.END, f"{key} {value}\n")


def remove_entry():
    name = entry1.get()
    try:
        count = int(entry2.get())
        if count <= 0 or (not name.isalpha()):
            clear_text_widget_and_buttons()
            text_widget.insert(tk.END, "Invalid input! You can only enter positive values!")
        else:
            remove(name, count)
    except ValueError:
        clear_text_widget_and_buttons()
        text_widget.insert(tk.END, "Invalid input! You can only enter valid values!")


def load_entry():
    name = entry1.get()
    try:
        count = int(entry2.get())
        if count <= 0 or (not name.isalpha()):
            clear_text_widget_and_buttons()
            text_widget.insert(tk.END, "Invalid input! You can only enter valid values!")
        else:
            load(name, count)
    except ValueError:
        clear_text_widget_and_buttons()
        text_widget.insert(tk.END, "Invalid input! You can only enter valid values!")


def clear_text_widget_and_buttons():
    text_widget.delete(1.0, tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)


def history_log():
    clear_text_widget_and_buttons()
    for item in history:
        text_widget.insert(tk.END, f"{item}\n")


def help_button():
    clear_text_widget_and_buttons()
    text_widget.insert(tk.END, "Welcome to this simple Warehouse Managing Tool:\n\nPress LOAD to enter\
 new quantities or new items entering your warehouse.\nPress REMOVE to\
 remove quantities from existing stock in the warehouse.\nPress AUDIT to\
 review existing items and quantities.\nPress HISTORY to\
 review the history of all successful transactions thus far.")


root = tk.Tk()
root.geometry("750x350")
root.title("Warehouse")

label = tk.Label(root, text="Warehouse Managing Tool", font=("Arial", 15))
label.pack()

# Create text widget
text_widget = tk.Text(root, height=7)
text_widget.pack(padx=20, pady=20)

# Create 2 entry windows:
entry_frame = tk.Frame(root)
entry_frame.pack(padx=20, pady=20)

label1 = tk.Label(entry_frame, text="Enter the item:")
label1.pack(side=tk.LEFT)
entry1 = tk.Entry(entry_frame)
entry1.pack(side=tk.LEFT)

label2 = tk.Label(entry_frame, text="Enter the quantity:")
label2.pack(side=tk.LEFT)
entry2 = tk.Entry(entry_frame)
entry2.pack(side=tk.LEFT)

# Create buttons:
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

button1 = tk.Button(button_frame, text="LOAD", font=("Arial", 15), command=load_entry)
button1.grid(row=0, column=0, sticky=tk.W+tk.E)

button2 = tk.Button(button_frame, text="REMOVE", font=("Arial", 15), command=remove_entry)
button2.grid(row=0, column=1, sticky=tk.W+tk.E)

button3 = tk.Button(button_frame, text="AUDIT", font=("Arial", 15), command=audit)
button3.grid(row=0, column=2, sticky=tk.W+tk.E)

button4 = tk.Button(button_frame, text="HISTORY", font=("Arial", 15), command=history_log)
button4.grid(row=1, column=0, sticky=tk.W+tk.E)

button5 = tk.Button(button_frame, text="HELP", font=("Arial", 15), command=help_button)
button5.grid(row=1, column=1, sticky=tk.W+tk.E)

button6 = tk.Button(button_frame, text="EXIT", font=("Arial", 15), bg="yellow", command=root.quit)
button6.grid(row=1, column=2, sticky=tk.W+tk.E)

button_frame.pack(fill="x")

root.mainloop()
