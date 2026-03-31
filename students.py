import md

students = []
yes = True

while yes:
    print("\033[1;34m==================== MENU TO USERS ====================\033[0m")
    print("""
    1. Regist new student.
    2. Show students list.
    3. Search student.
    4. Uptade student information.
    5. Remove student.
    6. Exit program.
""")
    option = input("Change a menu option: ")

    if option == "1":
        quantity = input("Quantity of students to add: ")
        while not quantity.isdigit():
            print("\033[1;31m¡DATA ERROR! TRY AGAIN\033[0m")
            quantity = input("Quantity of students to add: ")
        if int(quantity) < 1 :
            print("\033[1;31m¡ERROR! NUMBER 0 OR NEGATIVE, TRY AGAIN\033[0m")
            continue

        for s in range(int(quantity)):
            while yes:
                name = input("Enter the name of the student: ").lower()
                try:
                    age = int(input("Add the age student: "))
                except:
                    print("\033[1;31m¡DATA ERROR! TRY AGAIN!\033[0m")
                    continue

                program = input("Add the proram you belong to: ").lower()
                status = 0
                while status < 1 or status > 2:    
                    status = int(input("Choose status |\033[1;32m 1. active\033[0m/\033[1;31m 2. inactive\033[0m|: "))
                    # while not status.isdigit():
                    #     print("Choose a option between \033[1;32m1.\033[0m or \033[1;31m2.\033[0m")
                    #     status = input("Choose status |\033[1;32m 1. active\033[0m/\033[1;31m 2. inactive\033[0m|: ")
                    if status == 1:
                        status = "active"
                        print(f"status: \033[1;32m{status}\033[0m")
                        break
                    elif status == 2:
                        status = "inactive"
                        print(f"status: \033[1;31m{status}\033[0m")
                        break
                    elif not status:
                        print("Choose a option between \033[1;32m1.\033[0m or \033[1;31m2.\033[0m")
                        continue
                    else:
                        print("Choose a option between \033[1;32m1.\033[0m or \033[1;31m2.\033[0m")
                        continue
                if name == "" or program == "" or status == "":
                    print("\033[1;31m¡ERROR! EMPTY DATA, TRY AGAIN\033[0m")
                    continue
                if age < 1:
                    print("\033[1;31m¡ERROR! AGE IN 0 OR NEGATIVE, TRY AGAIN\033[0m")
                    continue
                else:
                    id = md.generate_id(students)
                    print("\n\033[1;32mREGISTERED STUDENT\033[0m")
                
                break
            md.students_record(students, id, name, age, program, status)
    
    elif option == "2":
        md.show_students(students)

    elif option == "3":
        if not students:
            print("students list empty")
        else:
            while yes:
                print("""
        1. Search for ID
        2. Search for name
        3. Enter '3' if you don't know the ID
        4. Exit
    """)
                search = input("choose a option: ")
                if search == "1":
                    id_search = int(input("Search for id of the student: "))
                    if id_search < len(students) or id_search > len(students):
                        continue
                    else:
                        md.search_student_id(students, id_search)     
                elif search == "2":
                    name_search = input("Search for name of the student: ").lower()
                    md.search_student_name(students, name_search)
                elif search == "3":
                    md.show_students(students)
                    
                else:
                    print("\033[1;31m¡DATA ERROR! TRY AGAIN\033[0m")
                    break
                    
    elif option == "4":
        change = input("change info? Y/N: ").lower()
        if change == "y":
            id_update = input("Enter the ID of the student:")
            md.update_info(students, id_update)
        elif change == "n":
            continue

    elif option == "5":
        id_remove = input("choose the ID for remove to the student:")
        md.remove_student(students, id_remove)
    
    elif option == "6":
        print("\033[1;34m==================== ¡EXIT PROGRAM! ====================\033[0m")
        break

    else:
        print("\033[1;31m¡DATA ERROR! TRY AGAIN!\033[0m")
