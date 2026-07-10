from tkinter import *
from tkinter import messagebox

contacts = []

# Load contacts
try:
    file = open("contacts.txt", "r")
    for line in file:
        contacts.append(line.strip().split(","))
    file.close()
except:
    pass

# Save contacts
def save_contacts():
    file = open("contacts.txt", "w")
    for contact in contacts:
        file.write(",".join(contact) + "\n")
    file.close()

# Display contacts
def show_contacts():
    listbox.delete(0, END)
    for contact in contacts:
        listbox.insert(END, f"{contact[0]} - {contact[1]}")

# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Enter Name and Phone")
        return

    contacts.append([name, phone, email, address])

    save_contacts()
    show_contacts()

    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

# Search contact
def search_contact():
    text = search_entry.get().lower()

    listbox.delete(0, END)

    for contact in contacts:
        if text in contact[0].lower() or text in contact[1]:
            listbox.insert(END, f"{contact[0]} - {contact[1]}")

# Delete contact
def delete_contact():
    try:
        index = listbox.curselection()[0]
        name = listbox.get(index).split(" - ")[0]

        for contact in contacts:
            if contact[0] == name:
                contacts.remove(contact)
                break

        save_contacts()
        show_contacts()

    except:
        messagebox.showwarning("Warning", "Select a contact")

# Update contact
def update_contact():
    try:
        index = listbox.curselection()[0]
        old_name = listbox.get(index).split(" - ")[0]

        for contact in contacts:
            if contact[0] == old_name:
                contact[0] = name_entry.get()
                contact[1] = phone_entry.get()
                contact[2] = email_entry.get()
                contact[3] = address_entry.get()
                break

        save_contacts()
        show_contacts()

    except:
        messagebox.showwarning("Warning", "Select a contact")


# GUI
root = Tk()
root.title("Contact Book")
root.geometry("500x600")

Label(root, text="Contact Book", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Name").pack()
name_entry = Entry(root, width=40)
name_entry.pack()

Label(root, text="Phone").pack()
phone_entry = Entry(root, width=40)
phone_entry.pack()

Label(root, text="Email").pack()
email_entry = Entry(root, width=40)
email_entry.pack()

Label(root, text="Address").pack()
address_entry = Entry(root, width=40)
address_entry.pack()

Button(root, text="Add Contact", width=20, command=add_contact).pack(pady=5)

Button(root, text="Update Contact", width=20, command=update_contact).pack(pady=5)

Button(root, text="Delete Contact", width=20, command=delete_contact).pack(pady=5)

Label(root, text="Search").pack()
search_entry = Entry(root, width=30)
search_entry.pack()

Button(root, text="Search Contact", width=20, command=search_contact).pack(pady=5)

Button(root, text="View All Contacts", width=20, command=show_contacts).pack(pady=5)

listbox = Listbox(root, width=60, height=15)
listbox.pack(pady=10)

show_contacts()

root.mainloop()
