# Mini Project- Create a contact book.

contactBook = {}
# create a contact
def createContact():
    name = input("Enter contact name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    contactBook[name] = {'Age': age, 'Email': email, 'Phone': phone}
    print("Contact created successfully!")

# read a contact
def readContact(name):
    if name in contactBook:
        print("Contact Mil gaya!")
        print("Age:" ,{contactBook[name]['Age']})
        print("Email:",{contactBook[name]['Email']})
        print("Phone:",{contactBook[name]['Phone']})
    else:
        print("Contact not found!",name)

# update a contact
def updateContact(name):
    if name in contactBook:
        age = input("Enter new age (warna press Enter to skip): ")
        email = input("Enter new email (warna press Enter to skip): ")
        phone = input("Enter new phone number (warna press Enter to skip): ")
        
        if age:
            contactBook[name]['Age'] = age
        if email:
            contactBook[name]['Email'] = email
        if phone:
            contactBook[name]['Phone'] = phone
        print("Contact updated successfully!",name)
    else:
        print("Contact not found!",name)

# delete a contact
def deleteContact(name):
    if name in contactBook:
        del contactBook[name]
        print("Contact deleted successfully!",name)
    else:
        print("Contact not found!",name)

# Main function 
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Create Contact")
        print("2. view Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice: ")

        # Perform action based on choice
        if choice == '1':
            createContact()
        elif choice == '2':
            name = input("Enter contact name: ")
            readContact(name)
        elif choice == '3':
            name = input("Enter contact name: ")
            updateContact(name)
        elif choice == '4':
            name = input("Enter contact name: ")
            deleteContact(name)
        elif choice == '5':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

# maine
main()