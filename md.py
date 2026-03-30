def students_record(students, id, name, age, program, status):

    students.append({
        'id': id,
        'name':  name,
        'age': age,
        'program': program,
        'status': status
    })

def show_students(students):
    if not students:
        print("students list empty")
    for student in (students):
        print(f"\033[1;34m{student['id']}.\033[0m name: {student['name']} | age: {student['age']} | program: {student['program']} | status: {student['status']}")

def search_student_id(students, id_search):
    if not students:
        print("students list empty")
    for student in students:
        if student.get('id') == int(id_search):
            print(f"\033[1;34m{student['id']}.\033[0m name: {student['name']} | age: {student['age']} | program: {student['program']} | status: {student['status']}")

def search_student_name(students, name_search):
    if not students:
        print("students list empty")
    for student in students:
        if student.get('name') == name_search:
            print(f"\033[1;34m{student['id']}.\033[0m name: {student['name']} | age: {student['age']} | program: {student['program']} | status: {student['status']}")

def update_info(students, id_search):
    while True:
        print("option to change:")
        print("""
        1. name:
        2. program:
        3. status
        4. Exit
    """)
        option = input("choose option")
        if option == "1":
            for student in students:
                if student.get('id') == int(id_search):
                    name = input("change name: ")
                    student.get('name') == name

        elif option == "2":
            for student in students:
                if student.get('id') == int(id_search):
                    program = input("change name: ")
                    student.get('program') == program

        elif option == "3":
            for student in students:
                if student.get('id') == int(id_search):
                    status = input("change name: ")
                    student.get('status') == status

        elif option == "4":
            break
        else:
            print("==========try again==========")
def remove_student(students, id_remove):
    for student in students:
        if student.get('id') == int(id_remove):
            students.remove(student)
            return f"student: {student['name']} remove to the list"
# Validation

def generate_id(students):
    id = len(students) + 1
    return id