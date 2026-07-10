from tkinter import *
from tkinter import messagebox

tasks = []

# Load tasks
try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except:
    pass

# Save tasks
def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

# Show tasks
def show_tasks():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

# Add task
def add_task():
    task = entry.get()

    if task == "":
        messagebox.showwarning("Warning", "Enter a task")
        return

    tasks.append("❌ " + task)
    entry.delete(0, END)
    show_tasks()
    save_tasks()

# Delete task
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        show_tasks()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

# Complete task
def complete_task():
    try:
        index = listbox.curselection()[0]

        if tasks[index].startswith("❌"):
            tasks[index] = tasks[index].replace("❌", "✔", 1)

        show_tasks()
        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task")


# Main Window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")

Label(root, text="To-Do List", font=("Arial", 20, "bold")).pack(pady=10)

entry = Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)

Button(root, text="Complete Task", width=20, command=complete_task).pack(pady=5)

Button(root, text="Delete Task", width=20, command=delete_task).pack(pady=5)

listbox = Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=20)

show_tasks()

root.mainloop()
