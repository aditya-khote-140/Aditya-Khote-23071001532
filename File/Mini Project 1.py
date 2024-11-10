# Mini Project- Create a fine System for your college


students = []

# add a new student and their fine amount
def add_student(name, fine_amount):
    students.append({"name": name, "fine": fine_amount})
    print(f"Student {name} added with a fine of ₹{fine_amount}.")

# update a student's fine
def update_fine(name, fine_amount):
    for student in students:
        if student["name"] == name:
            student["fine"] += fine_amount
            print(f"{name}'s fine updated by ₹{fine_amount}. Total fine is now ₹{student['fine']}.")
            return
    print(f"Student {name} not found.")

# remove fine for a student
def remove_fine(name):
    for student in students:
        if student["name"] == name:
            student["fine"] = 0
            print(f"Fine for {name} has been removed.")
            return
    print(f"Student {name} not found.")

# display all student fines
def display_fines():
    if not students:
        print("No students in the record.")
        return
    print("Student Fines:")
    for student in students:
        print(f"Name: {student['name']}, Fine: ₹{student['fine']}")

# calculate total fines
def total_fines():
    total = 0
    for student in students:
        total += student["fine"]
    print(f"Total fines collected: ₹{total}")

# Main Program
while True:
    print("\n--- College Fine System ---")
    print("1. Add Student Fine")
    print("2. Update Student Fine")
    print("3. Remove Student Fine")
    print("4. Display All Fines")
    print("5. Total Fines Collected")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        fine_amount = int(input("Enter fine amount: ₹"))
        add_student(name, fine_amount)

    elif choice == "2":
        name = input("Enter student name: ")
        fine_amount = int(input("Enter fine amount to add: ₹"))
        update_fine(name, fine_amount)

    elif choice == "3":
        name = input("Enter student name: ")
        remove_fine(name)

    elif choice == "4":
        display_fines()

    elif choice == "5":
        total_fines()

    elif choice == "6":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
