import mysql.connector as mc
import getpass
from tabulate import tabulate


'''

use/replace  the below code to hide password this will only work in terminal

getpass() function from getpass module
import getpass
password = getpass.getpass("enter your password: ")

or replace this when you are using it in idle
password = input("enter your password")


'''
password = getpass.getpass("enter your password: ")


def connection():
    mydb = mc.connect(host = "localhost",
                      user = "root",
                      passwd = password,
                      database = "hospital")
    if mydb.is_connected():
        return mydb
    return False


def generate(fn):
    functions = {'add_appointment': add_appointment, 'add_doctor': add_doctor, 'add_patient': add_patient, 'change_appointment': change_appointment, 'change_room': change_room, 'custom_query': custom_query, 'delete_app': delete_app, 'delete_doctor': delete_doctor, 'delete_patient': delete_patient, 'delete_room': delete_room, 'doc_change': doc_change, 'doc_edit': doc_edit, 'edit_appointment': edit_appointment, 'edit_room': edit_room, 'insert_room': insert_room, 'pat_change': pat_change, 'pat_edit': pat_edit, 'search_doctor': search_doctor, 'search_patient': search_patient, 'view_appointment': view_appointment, 'view_doctor': view_doctor, 'view_patient': view_patient, 'view_room': view_room}
    more = input("Accesss more data (Y/N): ")
    if more.upper() == "Y":
        how_many = int(input("Frequency: "))
        for i in range(how_many):
           functions[fn]()
        main_menu = input("press Y to go back to main menu or any key to exit: ")
        if main_menu.upper() == "Y":
            return True
        else:
            return exit()

    elif more.upper() == "N":
        main_menu = input("press Y to go back to main menu or any key to exit: ")
        if main_menu.upper() == "Y":
            return True
        else:
            return exit()
    else:
        print("incorrect key")
        return exit()
    

def success():
    print("""
    +-++-++-++-++-++-++-+
    |S||U||C||C||E||S||S|
    +-++-++-++-++-++-++-+
    """)


def failure():
    print("""
    +-++-++-++-++-++-++-+
    |F||A||I||L||U||R||E|
    +-++-++-++-++-++-++-+

    NO DATA FOUND 
    """)


def done():
    print("""
    +-++-++-++-+
    |D||O||N||E|
    +-++-++-++-+
    """)
    

def execute(query, printData = 0):
    mydb = connection()
    mycursor = mydb.cursor()

    mycursor.execute(query)
    
    rowCnt = mycursor.rowcount
    headers = mycursor.column_names
    
    data = mycursor.fetchall()
    if (len(data) > 0):
        print(tabulate(data, headers, tablefmt="psql"))
        rowCnt = 1
        
    if (rowCnt > 0 and printData):
        done()

    elif (rowCnt > 0):
        success()

    else:
        failure()

    mydb.commit()
    mycursor.close()
    mydb.close()


def add_doctor():

    doc_id = input("enter doctor id : ")
    doc_name = input("enter doctor name : ")
    doc_sirname = input("enter doctor sir name: ")
    doc_speciality = input("enter doctor speciality: ")
    doc_number = input("enter doctor number: ")
    doc_email = input("enter doctor email: ")
    doc_room = int(input("enter doctor room: "))
    doc_salary = int(input("enter doctor salary: "))

    query = "insert into doctor values('{}','{}','{}','{}','{}','{}',{}, {})".format(doc_id, doc_name, doc_sirname, doc_speciality, doc_number, doc_email, doc_room, doc_salary)
    execute(query)


def add_patient():

    pat_id = input("enter patient_id : ")
    pat_name = input("enter patient name: ")
    pat_sirname = input("enter patient sirname: ")
    pat_problem = input("enter patient problem: ")
    pat_number = input("enter patient number: ")
    pat_email = input("enter patient email:")
    pat_room = int(input("enter patient room: "))

    query = "insert into patient values('{}','{}','{}','{}','{}','{}',{})".format(pat_id, pat_name, pat_sirname, pat_problem, pat_number, pat_email, pat_room)
    execute(query)
    
    
def delete_doctor():
    
    doc_id = input("enter doctor id :")
    query = f"delete from doctor where doc_id = '{doc_id}'"
    execute(query)

    
def delete_patient():
    
    pat_id = input("enter patient id :")
    query = f"delete from patient where pat_id = '{pat_id}'"
    execute(query)


def custom_query():
    query = input("enter your custom query:")
    if "select" in query.lower():
        execute(query, 1)
    else:
        print("sorry cannot perform this action !!!")

        
def search_doctor():
    print("1 :  search doctor by id")
    print("2 :  search doctor by name")
    print("3 :  search doctor by surname")
    print("4 :  search doctor by speciality")
    print("5 :  search doctor by number")
    print("6 :  search doctor by email")
    print("7 :  search doctor by room")
    print("8 :  search doctor by salary")
    print("9 :  custom query")

    user = int(input("enter your choice: "))
    if user == 1:
        search_doctor = input("enter doctor id: ")
        query = f"select * from doctor where doc_id = '{search_doctor}'"

    elif user == 2:
        search_doctor = input("enter doctor name: ")
        query = f"select * from doctor where doc_name = '{search_doctor}'"

    elif user == 3:
        search_doctor = input("enter doctor sirname:")
        query = f"select * from doctor where doc_sirname ='{search_doctor}'"

    elif user == 4:
        search_doctor = input("enter doctor speciality: ")
        query = f"select * from doctor where doc_speciality = '{search_doctor}'"

    elif user == 5:
        search_doctor = input("enter doctor number: ")
        query = f"select * from doctor where doc_number = '{search_doctor}'"

    elif user == 6:
        search_doctor = input("enter doctor email: ") 
        query = f"select * from doctor where doc_email= '{search_doctor}'"

    elif user == 7:
        search_doctor = int(input("enter doctor room: "))
        query = f"select * from doctor where doc_room = {search_doctor}"

    elif user == 8:
        search_doctor = int(input("enter doctor salary: "))
        query = f"select * from doctor where doc_salary = {search_doctor}"

    elif user == 9:
        custom_query()
        return

    else:
        print("wrong input")
        return
    execute(query, 1)


def search_patient():
    print("1 :  search patient by id")
    print("2 :  search patient by name")
    print("3 :  search patient by sirname")
    print("4 :  search patient by problem")
    print("5 :  search patient by number")
    print("6 :  search patient by email")
    print("7 :  search patient by room")
    print("8 :  custom query")

    user = int(input("enter your choice: "))
    
    if user == 1:
        search_patient = input("enter pat id: ")
        query = f"select * from patient where pat_id = '{search_patient}'"

    elif user == 2:
        search_patient = input("enter patient name: ")
        query = f"select * from patient where pat_name = '{search_patient}'"

    elif user == 3:
        search_patient = input("enter pat sirname:")
        query = f"select * from patient where pat_sirname ='{search_patient}'"

    elif user == 4:
        search_patient = input("enter patient problem: ")
        query = f"select * from patient where pat_problem = '{search_patient}'"

    elif user == 5:
        search_patient = input("enter patient number: ")
        query = f"select * from patient where pat_number = '{search_patient}'"

    elif user == 6:
        search_patient = input("enter patient email: ")
        query = f"select * from patient where pat_email = '{search_patient}'"

    elif user == 7:
        search_patient = int(input("enter patient room: "))
        query = f"select * from patient where pat_room = {search_patient}"

    elif user == 8:
        custom_query()
        return
        
    else:
        print("wrong input")
        return
    execute(query, 1)


def view_doctor():
    print("1 :  Full information")
    print("2 :  view doctor names")
    print("3 :  doctor name and salary")
    print("4 :  doctor name and speciality")
    print("5 :  custom query")

    user = int(input("enter your choice: "))
    if user == 1:
        query = "select * from doctor"

    elif user == 2:
        query = "select doc_name from doctor"

    elif user == 3:
        query = "select doc_name, doc_salary from doctor"

    elif user == 4:
        query = "select doc_name, doc_speciality from doctor"

    elif user == 5:
        custom_query()
        return
    else:
        print("wrong input!!!")
        return
    execute(query, 1)
    
    
def view_patient():
    print("1 :  Full information")
    print("2 :  view patient_names")
    print("3 :  view patient name and room")
    print("4 :  patient_name and problem")
    print("5 :  custom query")

    user = int(input("enter your choice: "))
    if user == 1:
        query = "select * from patient"

    elif user == 2:
        query = "select pat_name from patient"

    elif user == 3:
        query = "select pat name, pat_room from patient"

    elif user == 4:
        query = "select pat_name, pat_problem from patient"

    elif user == 5:
        custom_query()
        return
    else:
        print("wrong input!!!")
        return
    
    execute(query, 1)

    
def doc_edit():
    print("1 :  edit doctor id")
    print("2 :  edit doctor name ")
    print("3 :  edit doctor sirname")
    print("4 :  edit doctor speciality")
    print("5 :  edit doctor number")
    print("6 :  edit doctor email")
    print("7 :  edit doctor room")
    print("8 :  edit doctor salary")
    print("9 :  custom query")

    user = int(input("enter your choice: "))
    if user == 1:
        doc_id = input("enter old doctor id : ")
        new_id = input("enter new doctor id : ")
        query = "update doctor set doc_id = '{}' where doc_id = '{}'".format(new_id, doc_id)

    elif user == 2:
        doc_id = input("enter doctor id :")
        doc_name = input("enter doctor name: ")
        query = f"update doctor set doc_name = '{doc_name}' where doc_id = '{doc_id}'"

    elif user == 3:
        doc_id = input("enter doctor id : ")
        doc_sirname = input("enter doctor sir name: ")
        query = f"update doctor set doc_sirname = '{doc_sirname}' where doc_id = '{doc_id}'"

    elif user == 4:
        doc_id = input("enter doctor id :")
        doc_speciality = input("enter doctor speciality: ")
        query = f"update doctor set doc_speciality = '{doc_speciality}' where doc_id = '{doc_id}'"
    
    elif user == 5:
        doc_id = input("enter doctor id :")
        doc_number = input("enter doctor number: ")
        query = f"update doctor set doc_number = '{doc_number}' where doc id = '{doc_id}'"
        
    elif user == 6:
        doc_id = input("enter doctor id :")
        doc_email = input("enter doctor email:")
        query = f"update doctor set doc_email = '{doc_email}' where doc_id = '{doc_id}'"
        
    elif user == 7:
        doc_id = input("enter doctor id : ")
        doc_room = int(input("enter doctor room: "))
        query = f"update doctor set doc_room = {doc_room} where doc_id = '{doc_id}'"
        
    elif user == 8:
        doc_id = input("enter doctor id : ")
        doc_salary = int(input("enter doctor salary: "))
        query = f"update doctor set doc_salary = {doc_salary} where doc_id = '{doc_id}'"
        
    elif user == 9:
        custom_query()
        return
    else:
        print("wrong input!!!")
        return

    execute(query, 1)
    
    
def pat_edit():
    print("1 :  edit patient id")
    print("2 :  edit patient name")
    print("3 :  edit patient sirname")
    print("4 :  edit patient problem")
    print("5 :  edit patient number")
    print("6 :  edit patient email")
    print("7 :  edit patient room")
    print("8 :  custom query")
    
    user = int(input("enter your choice: "))
    if user == 1:
        pat_id = input("enter old patient id : ")
        new_id = input("enter new patient id : ")
        
        query = f"update patient set pat_id = '{new_id}' where pat_id = '{pat_id}'"
        
    elif user == 2:
        pat_id = input("enter patient_id :")
        pat_name = input("enter patient name: ")
        query = f"update patient set pat_name = '{pat_name}' where pat_id = '{pat_id}"
        
    elif user == 3:
        pat_id = input("enter patient_id : ")
        pat_sirname = input("enter patient sir name: ")
        query = f"update patient set pat_sirname = '{pat_sirname}' where pat_id = '{pat_id}'"
        
    elif user == 4:
        pat_id = input("enter patient id :")
        pat_problem = input("enter patient problem: ")
        query = f"update patient set pat_problem = '{pat_problem}' where pat_id = '{pat_id}'"
        
    elif user == 5:
        pat_id = input("enter patient_id : ")
        pat_number = input("enter patient number: ")
        query = f"update patient set pat_number = '{pat_number}' where pat_id = '{pat_id}'"
        
    elif user == 6:
        pat_id = input("enter patient_id : ")
        pat_email = input("enter patient email: ")
        query = f"update patient set pat_email = '{pat_email}' where pat_id = '{pat_id}'"
        
    elif user == 7:
        pat_id = input("enter patient_id : ")
        pat_room = int(input("enter patient room: "))
        query = f"update patient set pat_room = {pat_room} where pat_id = '{pat_id}l'"
        
    elif user == 8:
        custom_query()
        return
    else:
        print("wrong input!!!")
        return
    execute(query, 1)


def doc_change():
    
    doc_id = input("enter doctor id : ")
    doc_name = input("enter doctor name :")
    doc_sirname = input("enter doctor sir name: ")
    doc_speciality = input("enter doctor speciality: ")
    doc_number = input("enter doctor number: ")
    doc_email = input("enter doctor email: ")
    doc_room = int(input("enter doctor room: "))
    doc_salary = int(input("enter doctor salary: "))
    query = f"update doctor set doc_id = '{doc_id}', doc_name = '{doc_name}', doc_sirname = '{doc_sirname}', doc_speciality = '{doc_speciality}', doc_number = '{doc_number}', doc_email = '{doc_email}', doc_room = {doc_room}, doc_salary {doc_salary} where doc_id = '{doc_id}'"
    execute(query)

    
def pat_change():
    
    pat_id = input("enter patient id : ")
    pat_name = input("enter patient name :")
    pat_sirname = input("enter patient sir name: ")
    pat_problem = input("enter patient problem: ")
    pat_number = input("enter patient number: ")
    pat_email = input("enter patient email: ")
    pat_room = int(input("enter patient room: "))
    query = f"update patient set pat_id = '{pat_id}', pat_name = '{pat_name}', pat_sirname = '{pat_sirname}', pat_problem = '{pat_problem}', pat_number = '{pat_number}', pat_email = '{pat_email}', pat_room = {pat_room} where pat_id = '{pat_id}'"
    execute(query)
    
    
def view_room():
    print("1 :  Full information")
    print("2 :  view room type")
    print("3 :  show available rooms")
    print("4 :  custom query")
    
    user = int(input("enter your choice: "))
    if user == 1:
        query = "select * from room"
        
    elif user == 2:
        query = "select room_assigned_for from room"
        
    elif user == 3:
        query = "select * from room where room_status = 'A'"
        
    elif user == 4:
        custom_query()
        return 
    else:
        print("wrong input")
        return
    execute(query, 1)
    
    
def edit_room():
    print("1 :  edit room id")
    print("2 :  edit room status")
    print("3 :  edit room assigned for/room type")
    print("4 :  edit room capacity")
    print("5 :  edit room number")
    print("6 :  custom query")
    
    user = int(input("enter your choice: "))
    if user == 1:
        room_id = input("enter old room id :")
        new_id = input("enter new room id : ")
        
        query = f"update room set room_id = '{new_id}' where room_id = '{room_id}'"
        
    elif user == 2:
        room_id = input("enter room id : ")
        ustatus = input("enter room status: ")
        query = f"update room set room_status = '{ustatus}' where room_id = '{room_id}'"
        
    elif user == 3:
        room_id = input("enter room id :")
        room_type = input("enter room type: ")
        query = f"update room set room_assigned_for '{room_type}' where room_id = '{room_id}'"
        
    elif user == 4:
        custom_query()
        return
    else:
        print("wrong input")
        return
    execute(query)
        
        
def change_room():
    
    room_id = input("enter room id : ")
    room_status = input("enter room status : ")
    room_assigned_for = input("enter room type/room assigned for: ")
    room_capacity = int(input("enter room capacity: "))
    
    room_no = int(input("enter room number: "))
    query = f"update room set room id = '{room_id}', room_status = '{room_status}',room_assigned_for =  '{room_assigned_for}', room_capacity = {room_capacity}, room_no = {room_no} where room_id = '{room_id}'"
    
    execute(query)

    
def delete_room():
    
    room_id = input("enter room id : ")
    query = f"delete from room where room_id = '{room_id}'"
    execute(query)

    
def insert_room():
    
    room_id = input("enter room id : ")
    room_status = input("enter room status :")
    room_assigned_for = input("enter room assigned for/type : ")
    room_capacity = int(input("enter room capacity : "))
    
    room_no = int(input("enter room number"))
    query = f"insert into room values('{room_id}','{room_status}','{room_assigned_for}', {room_capacity}, {room_no})"
    execute(query)
    print("\nNew room Successfully added!")

    
def add_appointment():
    
    app_id = input("enter appointment id : ")
    pat_name = input("enter patient name :")
    pat_sirname = input("enter patient sirname :")
    pat_problem = input("enter patient problem :")
    pat_number = input("enter patient number :")
    pat_email = input("enter patient email :")
    doctor = input("enter doctor name :")
    
    app_date = input("enter appointment date please use this format (YYYY-MM-DD): ")
    app_time = input("enter appointment time please use this format (HH:MM:SS): ")
    query = f"insert into appointment values('{app_id}','{pat_name}','{pat_sirname}', '{pat_problem}', '{pat_number}','{pat_email}','{doctor}', '{app_date}', '{app_time}')"
    
    execute(query)
    print("\nNew appointment Successfully added!")


def view_appointment():
    print("1 :  show all appointments")
    print("2 :  show appointment id , patient name and patient_sirname")
    print("3 :  show pat problem")
    print("4 :  show pat number")
    print("5 :  show pat email")
    print("6 :  show doctor")
    print("7 :  show appointment date")
    print("8 :  show appointment time")
    print("9 :  custom query")
    
    user = int(input("enter your choice: "))
    if user == 1:
        query = "select * from appointment"
        
    elif user == 2:
        query = "select app_id,pat_name, pat_sirname from appointment"
        
    elif user == 3:
        query = "select pat_problem from appointment"
       
    elif user == 4:
        query = "select pat_number from appointment"
        
    elif user == 5:
        query = "select pat_email from appointment"
        
    elif user == 6:
        query = "select doctor from appointment"
        
    elif user == 7:
        query = "select app date from appointment"
        
    elif user == 8:
        query = "select app_time from appointment"
        
    elif user == 9:
        custom_query()
        return
    else:
        print("wrong input!!!")
        return
    execute(query, 1)

    
def edit_appointment():
    print("1 :  edit appointment id")
    print("2 :  edit patient name and patient sirname")
    print("3 :  edit patient problem")
    print("4 :  edit pat number")
    print("5 :  edit pat email")
    print("6 :  edit doctor")
    print("7 :  edit appointment date")
    print("8 :  edit appointment time")
    print("9 :  custom query")
    
    user = int(input("enter your choice: "))
    if user == 1:
        app_id = input("enter old appointment id :")
        new_id = input("enter new appointment id : ")
        
        query = f"update appointment set app_id = '{new_id}' where app_id = '{app_id}'"
        
    elif user == 2:
        app_id = input("enter appointment id :")
        pat_name = input("enter patient name: ")
        pat_sirname = input("enter patient sirname: ")
        query = f"update appointment set pat_name = '{pat_name}', pat_sirname = '{pat_sirname}' where app_id {app_id}"
    
    elif user == 3:
        app_id = input("enter appointment id :")
        pat_problem = input("enter patient problem : ")
        query = f"update appointment set pat_problem = '{pat_problem}' where app_id = '{app_id}'"
    
    elif user == 4:
        app_id = input("enter appointment id : ")
        pat_number = input("enter patient number :")
        query = f"update appointment set pat_number = '{pat_number}' where app_id = '{app_id}'"
    
    elif user == 5:
        app_id = input("enter appointment id :")
        pat_email = input("enter email :")
        query = f"update appointment set pat_email = '{pat_email}' where app_id= '{app_id}'"
    
    elif user == 6:
        app_id = input("enter appointment id :")
        doctor = input("enter doctor name :")
        query = f"update appointment set doctor = '{doctor}' where app_id = '{app_id}'"
    
    elif user == 7:
        app_id = input("enter appointment id : ")
        app_date = input("enter appointment date please use this format (YYYY-MM-DD) :")
        query = f"update appointment set app_date = '{app_date}' where app_id= '{app_id}'"
    
    elif user == 8:
        app_id = input("enter appointment id : ")
        app_time = input("enter appointment time, please use this format (HH:MM:SS) :")
        query = f"update appointment set app_time = '{app_time}' where app_id = '{app_id}'"
    
    elif user == 9:
        custom_query()
        return
    else:
        print("wrong input")
        return
    execute(query)

def change_appointment():
   
    app_id = input("enter appointment id :")
    pat_name = input("enter patient name :")
    pat_sirname = input("enter patient sirname :")
    pat_problem = input("enter patient problem :")
    pat_number = input("enter patient number :")
    pat_email = input("enter patient email :")
    doctor = input("enter doctor name : ")
    app_date = input("enter appointment date please use this format (YYYY-MM-DD): ")
    app_time = input("enter appointment time please use this format (HH:MM:SS) :")
    query = f"update appointment set app_id = '{app_id}', pat_name = '{pat_name}', pat_sirname = '{pat_sirname}', pat_problem = '{pat_problem}', pat_number'{pat_number}', pat_email = '{pat_email}', doctor = '{doctor}', app_date = '{app_date}',app_time = '{app_time}' where app_id = '{app_id}'"
    execute(query)


def delete_app():
    app_id = input("enter appointment id : ")
    query = f"delete from appointment where app_id = '{app_id}'"
    execute(query)


def generate(fn):
    functions = {'add_appointment': add_appointment, 'add_doctor': add_doctor, 'add_patient': add_patient, 'change_appointment': change_appointment, 'change_room': change_room, 'custom_query': custom_query, 'delete_app': delete_app, 'delete_doctor': delete_doctor, 'delete_patient': delete_patient, 'delete_room': delete_room, 'doc_change': doc_change, 'doc_edit': doc_edit, 'edit_appointment': edit_appointment, 'edit_room': edit_room, 'insert_room': insert_room, 'pat_change': pat_change, 'pat_edit': pat_edit, 'search_doctor': search_doctor, 'search_patient': search_patient, 'view_appointment': view_appointment, 'view_doctor': view_doctor, 'view_patient': view_patient, 'view_room': view_room}
    more = input("Accesss more data (Y/N): ")
    if more.upper() == "Y":
        how_many = int(input("Frequency: "))
        for i in range(how_many):
           functions[fn]()

        main_menu = input("press Y to go back to main menu or any key to exit: ")
        if main_menu.upper() == "Y":
            return True
        else:
            return exit()

    elif more.upper() == "N":
        main_menu = input("press Y to go back to main menu or any key to exit: ")
        if main_menu.upper() == "Y":
            return True
        else:
            return exit()
    else:
        print("incorrect key")
        return exit()
