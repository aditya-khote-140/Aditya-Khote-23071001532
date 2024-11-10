# create a contact
contactBook = {}
def createContact():
    name = input("Enter contact name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    contactBook[name] = {'Age': age, 'Email': email, 'Phone': phone}
    print("Contact created successfully!")
    
    def readContact(name):
        if name in contactBook:
            print("Contact Mil gaya!")
            print("Age: {contactBook[name]['Age']}")
            print("Email: {contactBook[name]['Email']}")
            print("Phone: {contactBook[name]['Phone']}")
        else:
            print("Contact not found!",name)
        
        
    def main():
        while True:
            print("\nContact Book Menu:")
            print("1. Create Contact")
            print("2. Read Contact")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Exit")
            
        # user choice
    choice = input("Enter your choice: ")

        # action choice
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