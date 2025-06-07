import tkinter as tk
from tkinter import messagebox, filedialog
import os
from datetime import datetime

# Add a task with due date
def add_task():
    task = task_entry.get().strip() # type: ignore
    due = due_entry.get().strip()

    if task:
        if due:
            try:
                # Try parsing date
                due_date = datetime.strptime(due, "%Y-%m-%d")
                task_text = f"{task} (Due: {due_date.strftime('%b %d')})"
            except ValueError:
                messagebox.showwarning("Date Format Error", "Use format YYYY-MM-DD")
                return
        else:
            task_text = task
        listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END) # type: ignore
        due_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Mark selected task as done
def mark_done():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        if not task.endswith(" ✓"):
            listbox.delete(selected)
            listbox.insert(selected, task + " ✓")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Save tasks to a file
def save_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            tasks = listbox.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")

# Load tasks from a file
def load_tasks():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt")])
    if file_path and os.path.exists(file_path):
        with open(file_path, "r") as f:
            listbox.delete(0, tk.END)
            for line in f:
                listbox.insert(tk.END, line.strip())

# Setup main window
root = tk.Tk()
root.title("🌟 My To-Do List app")
root.geometry("350x500")
root.configure(bg="#e6f7ff")  # Light blue background

# Style
label_style = {"bg": "#1e1e1e", "fg": "#ffffff", "font": ("Arial", 12)}
entry_style = {"bg": "#2e2e2e", "fg": "#ffffff", "insertbackground": "white", "font": ("Arial", 12)}

tk.Label(root, text="📝 Task:", **label_style).pack(pady=(10, 0))
task_entry = tk.Entry(root, **entry_style, width=30)
task_entry.pack(pady=5)

tk.Label(root, text="📅 Due Date (YYYY-MM-DD):", **label_style).pack() # type: ignore
due_entry = tk.Entry(root, **entry_style, width=30) # type: ignore
due_entry.pack(pady=5)


# Header
header = tk.Label(root, text="📋 TO-DO LIST", font=("Arial", 18, "bold"), bg="#e6f7ff", fg="#003366")
header.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=25, font=("Arial", 14), bg="#ffffff", fg="#000000")
entry.pack(pady=10)

# Buttons with colors
button_style = {"font": ("Arial", 11, "bold"), "width": 20, "padx": 5, "pady": 5}

tk.Button(root, text="Add Task", bg="#4CAF50", fg="white", command=add_task, **button_style).pack(pady=4)
tk.Button(root, text="Delete Task", bg="#f44336", fg="white", command=delete_task, **button_style).pack(pady=4)
tk.Button(root, text="Mark as Done", bg="#2196F3", fg="white", command=mark_done, **button_style).pack(pady=4)
tk.Button(root, text="Save Tasks", bg="#FF9800", fg="white", command=save_tasks, **button_style).pack(pady=4)
tk.Button(root, text="Load Tasks", bg="#9C27B0", fg="white", command=load_tasks, **button_style).pack(pady=4)

# Task Listbox
listbox = tk.Listbox(root, font=("Arial", 12), width=32, height=12, bg="#fff", fg="#333")
listbox.pack(pady=10)

root.mainloop()
