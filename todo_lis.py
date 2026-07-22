import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# ---------------------- Functions ----------------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(tk.END, task)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        json.dump(list(tasks), file)

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    listbox.insert(tk.END, "⬜ " + task)
    task_entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def mark_completed():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)

        if task.startswith("⬜"):
            task = task.replace("⬜", "✅", 1)
            listbox.delete(index)
            listbox.insert(index, task)
            save_tasks()
        else:
            messagebox.showinfo("Info", "Task already completed!")

    except:
        messagebox.showwarning("Warning", "Please select a task!")

def clear_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

# ---------------------- GUI ----------------------

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x550")
root.config(bg="#f2f2f2")
root.resizable(False, False)

title = tk.Label(
    root,
    text="📝 TO-DO LIST",
    font=("Arial", 20, "bold"),
    bg="#4CAF50",
    fg="white",
    pady=10
)
title.pack(fill=tk.X)

task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=15, padx=20, fill=tk.X)

add_btn = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=add_task
)
add_btn.pack(pady=5)

listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=15,
    selectbackground="#4CAF50"
)
listbox.pack(pady=10)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack()

complete_btn = tk.Button(
    frame,
    text="Complete",
    bg="#2196F3",
    fg="white",
    width=12,
    command=mark_completed
)
complete_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(
    frame,
    text="Delete",
    bg="#F44336",
    fg="white",
    width=12,
    command=delete_task
)
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(
    frame,
    text="Clear All",
    bg="#FF9800",
    fg="white",
    width=12,
    command=clear_all
)
clear_btn.grid(row=0, column=2, padx=5)

load_tasks()

root.mainloop()