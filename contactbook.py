import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Simple Contact Manager")
root.geometry("400x450")
root.configure(bg="#c3b3c8")

# Contact data storage (in-memory)
contacts = {}
def validate_phone(proposed):
    if proposed.isdigit() or proposed == "":
        return True
    messagebox.showerror("Invalid Input", "Phone must contain only digits.")
    return False

phone_vcmd = (root.register(validate_phone), '%P')
def validate_name(proposed):
    if proposed.isalpha() or proposed == "":
        return True
    messagebox.showerror("Invalid Input", "Name must contain only letters.")
    return False
name_vcmd = (root.register(validate_name), '%P')


# Functions to handle contact operations
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    if name and phone:
        contacts[name] = phone
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "Please enter both name and phone number.")

def update_contact_list():
    listbox.delete(0, tk.END)
    for name, phone in contacts.items():
        listbox.insert(tk.END, f"{name}: {phone}")

def on_select(event):
    selected = listbox.curselection()
    if selected:
        name = listbox.get(selected[0]).split(":")[0]
        phone = contacts[name]
        name_var.set(name)
        phone_var.set(phone)

def delete_contact():
    selected = listbox.curselection()
    if selected:
        name = listbox.get(selected[0]).split(":")[0]
        del contacts[name]
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

def clear_fields():
    name_var.set("")
    phone_var.set("")

# UI Elements
name_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(root, text="Name:", bg="lightyellow").pack(pady=(20,0))
name_entry = tk.Entry(root, textvariable=name_var,
                      validate="key", validatecommand=name_vcmd)
name_entry.pack(pady=(0,10), padx=10)


tk.Label(root, text="Phone:", bg="lightyellow").pack(pady=(10,0))
phone_entry = tk.Entry(root, textvariable=phone_var,
                       validate="key", validatecommand=phone_vcmd)
phone_entry.pack(pady=(0,10), padx=10)
tk.Button(root, text="Add Contact",bg="#E9967A",fg="black", command=add_contact).pack(pady=(5,15))
tk.Label(root, text="Contacts:").pack()
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=(0,10), padx=10)
listbox.bind('<<ListboxSelect>>', on_select)

tk.Button(root, text="Delete Selected",bg="#33c294",fg="black",command=delete_contact).pack(pady=5)
tk.Button(root, text="Clear Fields",bg="#33c294",fg="black", command=clear_fields).pack(pady=5)

root.mainloop()
