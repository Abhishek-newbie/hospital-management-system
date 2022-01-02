from main_functions import *


try:
    if connection():
        while True:
            try:


                print("================================================================================")
                print("________________________________________________________________________________")
                print("                         WELCOME TO OUR HOSPITAL")
                print("                     WHAT WOULD YOU LIKE TO DO TODAY")
                print("                                 ⓿_⓿            ")
                print("________________________________________________________________________________")
                print("")
                print("================================================================================")
                print()
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
                        more = input("wanna add more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how much data you wanted to add: "))
                            for i in range(how_many):
                                add_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                            
                        elif more.upper() == "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        else:    
                            print("incorrect key")
                            break
                    elif user== 2:
                        view_doctor()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    
                    elif user == 3:
                        doc_edit()
                        more = input("wanna edit more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to edit the data:"))
                            for i in range(how_many):
                                doc_edit()
                                main_menu = input("press Y to go back to main menu or any key to exit: ")
                                if main_menu.upper() == "Y":
                                    continue
                                else:
                                    break
                        elif more.upper() == "N":
                            
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break

                    elif user == 4:
                        doc_change()
                        more = input("wanna edit more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to edit the data:"))
                            for i in range(how_many):
                                doc_edit()
                                main_menu = input("press Y to go back to main menu or any key to exit: ")
                                if main_menu.upper() == "Y":
                                    continue
                                else:
                                    break
                        elif more.upper() == "N":
                            
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 5:
                        delete_doctor()
                        more = input("wanna edit more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to edit the data:"))
                            for i in range(how_many):
                                doc_edit()
                                main_menu = input("press Y to go back to main menu or any key to exit: ")
                                if main_menu.upper() == "Y":
                                    continue
                                else:
                                    break
                        elif more.upper() == "N":
                            
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 6:
                        search_doctor()
                        more = input("wanna edit more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to edit the data:"))
                            for i in range(how_many):
                                doc_edit()
                                main_menu = input("press Y to go back to main menu or any key to exit: ")
                                if main_menu.upper() == "Y":
                                    continue
                                else:
                                    break
                        elif more.upper() == "N":
                            
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 7:
                        custom_query()
                        more = input("wanna go for custom query (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to go for custom queries: "))
                            for i in range(how_many):
                                custom_query()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()=="N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 8:
                        continue
                    elif user == 9:
                        break
                    else:
                        print("incorrect key")

                    
                if user == 2:
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
                        more =input("wanna add more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how much data you wanted to add: "))
                            for i in range(how_many):
                                add_patient()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()=="Y":
                                continue
                            else:
                                break
                        elif more.upper() == "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 2:
                        view_patient()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 3:
                        pat_edit()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user ==  4:
                        pat_change()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 5:
                        delete_patient()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                        
                    elif user == 6:
                        search_patient()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 7:
                        custom_query()
                        more = input("wanna go for custom query (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to go for custom queries: "))
                            for i in range(how_many):
                                custom_query()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()=="N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 8:
                        continue
                    elif user == 9:
                        break
                    else:
                        print("incorrect key")

                    
                if user == 3:
                    
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
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 2:
                        view_roommore = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 3:
                        edit_room()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 4:
                        change_room()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 5:
                        delete_room()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 6:
                        custom_query()
                        more = input("wanna go for custom query (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to go for custom queries: "))
                            for i in range(how_many):
                                custom_query()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()=="N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                        
                    elif user == 7:
                        continue
                    elif user == 8:
                        break
                    else:
                        print("incorrect key")
                        break
                

                if user ==4:
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
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 2:
                        view_appointment()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    
                    elif user == 3:
                        edit_appointment()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 4:
                        change_appointment()
                        more = input("wanna change more data (Y/N): ")
                        if more.upper() == "Y":
                            more = input("wanna view more data (Y/N): ")
                            if more.upper() == "Y":
                                how_many = int(input("how many times you wanted to view the data:"))
                                for i in range(how_many):
                                    view_doctor()
                                main_menu = input("press Y to go back to main menu or any key to exit: ")
                                if main_menu.upper() == "Y":
                                    continue
                                else:
                                    break
                            elif more.upper()== "N":
                                main_menu = input("press Y to go back to main menu or any key to exit: ")
                                if main_menu.upper()== "Y":
                                    continue
                                else:
                                    break
                            else:
                                print("incorrect key")
                                break
                    elif user== 5:
                        delete_appo()
                        more = input("wanna view more data (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to view the data:"))
                            for i in range(how_many):
                                view_doctor()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()== "N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper()== "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                        
                    elif user == 6:
                        custom_query()
                        more = input("wanna go for custom query (Y/N): ")
                        if more.upper() == "Y":
                            how_many = int(input("how many times you wanted to go for custom queries: "))
                            for i in range(how_many):
                                custom_query()
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        elif more.upper()=="N":
                            main_menu = input("press Y to go back to main menu or any key to exit: ")
                            if main_menu.upper() == "Y":
                                continue
                            else:
                                break
                        else:
                            print("incorrect key")
                            break
                    elif user == 7:
                        continue
                    elif user == 8:
                        break
                    else:
                        print("incorrect key")
                        break
                    
                elif user == 5:
                    print("under construction")
                    break
                elif user == 6:
                    print(" (about)under construction!!!")
                    break
                elif user == 7:
                    print("(license)under construction!!!")
                    break
                elif user == 8:
                    break
                else:
                    print("wrong input")
                    break
            except:
                print("an error occured !!! please check your data or input or for any inconvenience check help in main menu")
                continue
except:
    print("please check your password again !!!")

