from functions import *


running = False

try:
    if (connection()):
        running = True
except Exception as e:
    print(e, "check your password again !!")

while running:
    try:
        print("==========================================================================================")
        print("                              :::::::::::::::::")
        print('''
         __      __ ___  _      ___   ___   __  __  ___ 
         \ \    / /| __|| |    / __| / _ \ |  \/  || __|
          \ \/\/ / | _| | |__ | (__ | (_) || |\/| || _| 
           \_/\_/  |___||____| \___| \___/ |_|  |_||___| ''')

        print()
        print("                    ---------------------------------------")
        print("                       WHAT WOULD YOU LIKE TO DO TODAY  ^_^ ")
        print("                    ---------------------------------------")
        print()
        print("                              :::::::::::::::::")
        print("==========================================================================================")
        print("1. DOCTOR")
        print("2. PATIENT")
        print("3. ROOM")
        print("4. APPOINTMENT")
        print("5. HELP")
        print("6. ABOUT")
        print("7. LICENSE")
        print("8. EXIT")
        
        user = int(input("enter your choice: "))
        if user == 1:
            print("1. ADD DOCTOR")
            print("2. VIEW DOCTOR")
            print("3. EDIT DOCTOR")
            print("4. CHANGE DOCTOR")
            print("5. DELETE DOCTOR")
            print("6. SEARCH DOCTOR")
            print("7. CUSTOM QUERY")
            print("8. BACK TO MAIN MENU")
            print("9. EXIT")
            
            user = int(input("enter your choice: "))
            if user == 1:
                add_doctor()
                generate('add_doctor')

            elif user == 2:
                view_doctor()
                generate('view_doctor')

            elif user == 3:
                doc_edit()
                generate('doc_edit')

            elif user == 4:
                doc_change()
                generate('doc_change')

            elif user == 5:
                delete_doctor()
                generate('delete_doctor')

            elif user == 6:
                search_doctor()
                generate('search_doctor')

            elif user == 7:
                custom_query()
                generate('custom_query')
                continue

            else:
                print("incorrect key")
                break

        elif user == 2:
            print("1. ADD PATIENT")
            print("2. VIEW PATIENT")
            print("3. EDIT PATIENT")
            print("4. CHANGE PATIENT")
            print("5. DELETE PATIENT")
            print("6. SEARCH PATIENT")
            print("7. CUSTOM QUERY")
            print("8. BACK TO MAIN MENU")
            print("9. EXIT")

            user = int(input("enter your choice: "))
            if user == 1:
                add_patient()
                generate('add_patient')

            elif user == 2:
                view_patient()
                generate('view_patient')

            elif user == 3:
                pat_edit()
                generate('pat_edit')

            elif user == 4:
                pat_change()
                generate('pat_change')

            elif user == 5:
                delete_patient()
                generate('delete_patient')

            elif user == 6:
                search_patient()
                generate('search_patient')

            elif user == 7:
                custom_query()
                generate('custom_query')

            elif user == 8:
                continue
        
            else:
                print("incorrect key")
                break
                    
        elif user == 3:
            print("1. ADD ROOM")
            print("2. VIEW ROOM")
            print("3. EDIT ROOM")
            print("4. CHANGE ROOM")
            print("5. DELETE ROOM")
            print("6. CUSTOM QUERY")
            print("7. BACK TO MAIN MENU")
            print("8. EXIT")
            user = int(input("enter your choice: "))
            if user == 1:
                insert_room()
                generate('insert_room')

            elif user == 2:
                view_room()
                generate('view_room')

            elif user == 3:
                edit_room()
                generate('edit_room')

            elif user == 4:
                change_room()
                generate('change_room')

            elif user == 5:
                delete_room()
                generate('delete_room')

            elif user == 6:
                custom_query()
                generate('custom_query')

            elif user == 7:
                continue;

            else:
                print("incorrect key")
                break

        elif user == 4:
            print("1. ADD APPOINTMENT")
            print("2. VIEW APPOINTMENT")
            print("3. EDIT APPOINTMENT")
            print("4. CHANGE APPOINTMENT")
            print("5. DELETE APPOINTMENT")
            print("6. CUSTOM QUERY")
            print("7. BACK TO MAIN MENU")
            print("8. EXIT")
            user = int(input("enter your choice: "))
            if user == 1:
                add_appointment()
                generate('add_appointment')

            elif user == 2:
                view_appointment()
                generate('view_appointment')

            elif user == 3:
                edit_appointment()
                generate('edit_appointment')

            elif user == 4:
                change_appointment()
                generate('change_appointment')

            elif user== 5:
                delete_app()
                generate('delete_app')

            elif user == 6:
                custom_query()
                generate('custom_query')

            elif user == 7:
                continue

            elif user == 8:
                break
                    
        elif user == 5:
            print("under conuction")

        elif user == 6:
            print("(about) under conuction!!!")

        elif user == 7:
            print("(license) under conuction!!!")

        elif user == 8:
            break

        else:
            print("wrong input")
            break

    except Exception as e:
        print(e)

