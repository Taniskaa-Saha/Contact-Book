import tkinter as tk

contact = {}

def display_contact():
    print("name:\tcontact")
    for key in contact:
        print("{}\t{}".format(key, contact[key]))

root = tk.Tk()
root.title('CONTACT BOOK')
root.geometry('300x300')


text_display = tk.Text(root, height=2, width=16, font=('Arial Black', 24))
text_display.grid(columnspan=5)

while True:
    print("\n1. Add Contact\n2. Display Contacts\n3. Search Contact\n4. Update contact\n5. Delete Contact")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input ("Enter name:")
        phone = input("Enter phone number:")
        email = input("Enter email:")
        address = input("Enter address:")
        contact[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")
    elif choice == 2:
        if len(contact) == 0:
            print("No contacts found!")
        else:
            display_contact()
    elif choice == 3:
        name = input("Enter name to search:")
        if name in contact:
            print("Phone:", contact[name]["phone"] )
            print("Email:", contact[name]["email"])
            print("Address:", contact[name]["address"])
        else:
            print("Contact not found!")
    elif choice == 4:
        name = input("Enter name to be updated:")
        if name in contact:
            phone = input("Enter new phone number:")
            email = input("Enter new email:")
            address = input("Enter new address:")
            contact[name] = {"phone": phone, "email": email, "address": address}
            print("Contact updated successfully!")
        else:
            print("Contact not found!")
    elif choice == 5:
        name = input("Enter name to be deleted:")
        if name in contact:
            confirm = input("Are you sure you want to delete this contact yes/no?")
            if confirm == "yes" or confirm == "YES":
                del contact[name]
                print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    else:
        break
root.mainloop()
    