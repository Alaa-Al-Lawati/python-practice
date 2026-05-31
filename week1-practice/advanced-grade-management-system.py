grades = {
    "Ali": 78,
    "Sara": 45,
    "John": 90
}

def display_menu():
    pass

def add_student():
    name = input("Please enter the name: ")
    score = int(input("Please enter the grade: "))
    grades[name] = score
    print("Student added.")


def delete_student():
    name = input("Enter student to remove: ")

    if name in grades: 
        del grades[name]
        print("Student removed.")
    else:
        print("Student not found.")

def update():
    name = input("Enter student to alter grade: ")

    if name in grades:
        new_score = int(input("What's the new score? "))
        grades[name] = new_score 
        print("Grade updated.")
    else: 
        print("Student not found")
    

def view_students(): 
    print("\nStudents:")

    for name, score in grades.items(): 
        print(f"{name}: {score}")

def highest_grade(): 
    highest = max(grades.values())

    for name, score in grades.items():
        if score == highest: 
            print(f"Highest: {name} ({score})")

def lowest_grade(): 
    lowest = min(grades.values())

    for name, score in grades.items():
        if score == lowest: 
            print(f"Lowest: {name} ({score})")

def average_grade(): 
    average = sum(grades.values()) / len(grades)
    print(f"Average: {average:.2f}")

def passed_students(): 
    print("\nStudents who passed: ")
    for name, score in grades.items(): 
        if score >= 50: 
            print(f"{name} : ({score})")

def sort_students(): 
    sorted_grades = sorted(grades.items(), key= lambda item: item[1], reverse = True)
    print("\nSorted Studentd: ")

    for name, score in sorted_grades: 
        print(f"{name}: {score}")


while True: 
    choice = input("Choose: ")
    if choice == "1":
        add_student()

    elif choice == "2":
        delete_student()

    elif choice == "3":
        update()

    elif choice == "4":
        view_students()

    elif choice == "5":
        highest_grade()

    elif choice == "6":
        lowest_grade()

    elif choice == "7":
        average_grade()

    elif choice == "8":
        passed_students()

    elif choice == "9":
        sort_students()

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")