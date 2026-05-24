grades = {}

def add_student():
    name = input("Enter student name: ")
    score = float(input("Enter score: "))
    grades[name] = score
    print(f"{name} added with score {score}")

def show_grades():
    for name, score in grades.items():
        print(f"{name}: {score}")

while True:
    print("\n1. Add Student 2. Show Grades 3. Exit")
    choice = input("Choose: ")
    if choice == "1": add_student()
    elif choice == "2": show_grades()
    elif choice == "3": break
