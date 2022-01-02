import mysql.connector as mc
from tabulate import tabulate


password = input("enter your password: ")
def connection():
    mydb = mc.connect(host = "localhost",
                      user = "root",
                      passwd = password,
                      database = "hospital")
    if mydb.is_connected():
        return mydb

def add_doctor():
    mydb = connection()
    mycursor = mydb.cursor()
    doc_id = input("enter doctor_id : ")
    doc_name = input("enter doctor name : ")
    doc_sirname = input("enter doctor sir name: ")
    doc_speciality = input("enter doctor speciality: ")
    doc_number = input("enter doctor number: ")
    doc_email = input("enter doctor email: ")
    doc_room = int(input("enter doctor room: "))
    doc_salary = int(input("enter doctor salary: "))
    query = "insert into doctor values('{}','{}','{}','{}','{}','{}',{},{})".format(doc_id, doc_name,doc_sirname,doc_speciality,doc_number,doc_email, doc_room,doc_salary)
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("\nNew doctor Added Successfully !")
    
def add_patient():
    mydb = connection()
    mycursor = mydb.cursor()
    pat_id = input("enter patient_id : ")
    pat_name = input("enter patient name: ")
    pat_sirname = input("enter patient sir name: ")
    pat_problem = input("enter patient problem: ")
    pat_number = input("enter patient number: ")
    pat_email = input("enter patient email:")


    pat_room = int(input("enter patient room: "))
    query = "Insert Into patient values(0.00.0.0.0.0)".format(patid, pat_name,
    pat_sirname, pat_problem, pat_number, pat_email, pat_room)
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("\nNew patient Added Successfully !")
    
def delete_doctor():
    mydb = connection()
    mycursor = mydb.cursor()
    doc_id = input("enter doctor_id :")
    query = f"delete from doctor where doc_id = '{doc_id}'"
    data = mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    if not data:
        print("no such data found")
    else:
        print("deleted Successfully !")
    
def delete_patient():
    mydb = connection()
    mycursor = mydb.cursor()
    pat_id = input("enter patient_id :")
    query = f"delete from patient where pat_id = '{pat_id}'"
    data = mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    if not data:
        print("no such data found")
    else:
        print("deleted Successfully !")

def custom_query():
    mydb = connection()
    mycursor = mydb.cursor()
    custom_query = input("enter your custom query:")
    if "select" in custom_query.lower():
        mycursor.execute(custom_query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    else:
        print("sorry cannot perfom this action !!!")
        
def search_doctor():
    print("1 : search doctor by id")
    print("2 : search doctor by name")
    print("3 : search doctor by sirname")
    print("4 : search doctor by speciality")
    print("5: search doctor by number")
    print("6 : search doctor by email")
    print("7 : search doctor by room")
    print("8: search doctor by salary")
    print("9: custom query")
    mydb = connection()
    
    mycursor = mydb.cursor()
    user31 = int(input("enter your choice: "))
    if user31 == 1:
        search_doctor = input("enter doc_id: ")
        query = f"select * from doctor where doc_id = '{search_doctor}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers,tablefmt = "psql"))
            print("done !")
            
    elif user31 == 2:
        search_doctor = input("enter doctor name: ")
        query = f"select * from doctor where doc_name = '{search_doctor}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
            
    elif user31 == 3:
        search_doctor = input("enter doc sirname:")
        query = f"select * from doctor where doc_sirname ='{search_doctor}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers, tablefmt = "psql"))
            print("done !")

    elif user31 == 4:
        search_doctor = input("enter doc speciality: ")
        query = f"select * from doctor where doc_speciality = '{search_doctor}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
            
    elif user31 == 5:
        search_doctor = input("enter doc number: ")
        query = f"select * from doctor where doc_number = '{search_doctor}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user31 == 6:
        search_doctor = input("enter doc email: ") 
        query = f"select * from doctor where doc_email= '{search_doctor}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        mycursor.fetchall()
        data = mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers,tablefmt = "psql"))
            print("done !")
    elif user31 - 7:
        search_doctor = int(input("enter doc room: "))
        query = f"select * from doctor where doc_room - {search_doctor}"
        mycursor.execute(query)
        headers = myeursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
            
    elif user31 == 8:
        search_doctor = int(input("enter doc salary: "))
        query = f"select * from doctor where doc_salary = {search_doctor}"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
    elif user31 == 9:
            custom_query()
    else:
            print("wrong input")
            
            
def search_patient():
    print("1 : search patient by id")
    print("2 : search patient by name")
    print("3 : search patient by sirname")
    print("4 : search patient by problem")
    print("5 : search patient by number")
    print("6 : search patient by email")
    print("7: search patient by room")
    print("8: custom query")

    mydb = connection()
    mycursor = mydb.cursor()
    user31 = int(input("enter your choice: "))
    if user31 == 1:
        search_patient = input("enter pat id: ")
        query = f"select * from patient where pat_id = '{search_patient}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers, tablefmt = "psql"))
            print("done !")
    elif user31 == 2:
        search_patient = input("enter patient name: ")
        query = f"select * from patient where pat_name = '{search_patient}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
           print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
    elif user31 == 3:
        search_patient = input("enter pat sirname: ")
        query= f"select * from patient where pat_sirname = '{search_patient}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
        
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user31 == 4:
        search_patient = input("enter pat problem: ")
        query = f"select * from patient where pat_problem = '{search_patient}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        13

        data - mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers, tablefmt - "psqi"))
            print("done !")
    elif user31 == 5:
        search_patient = input("enter pat number: ")
        query = f"select * from patient where pat_number = '{search_patient}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
    elif user31 == 6:
        search_patient = input("enter pat email:")
        query= f"select * from patient where pat_email= '{search_patient}'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user31 == 7:
        search_patient = int(input("enter pat room: "))
        query = f"select * from patient where pat_room = {search_patient}"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            dfdd
        else:
            print("no such data found")
            print(tabulate(data, headers,tablefmt = "psql"))
            14

        print("done !")
    elif user31 * 8:
            custom_query
    else:
        print("wrong input")
    
def view_doctor():
    print("1 : Full information")
    print("2: view doc_names")
    print("3: doc_name and salary")
    print("4: doc_name and speciality")
    print("5: custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user11 = int(input("enter your choice: "))
    if user11 == 1:
        mycursor.execute("select * from doctor")
        headers = mycursor.column_names
        
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
    elif user11 == 2:
        mycursor.execute("select doc_name from doctor")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 3:
        mycursor.execute("select doc_name,doc_salary from doctor")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:

            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 4:
        headers = mycursor.column_names
        mycursor.execute("select doc_name, doc speciality from doctor")
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 5:
        custom_query()
    else:
        print("wrong input!!!")
    
    
def view_patient():
    print("1 : Full information")
    print("2 : view patient_names")
    print("3 : view patient name and room")
    print("4 : patient_name and problem")
    print("5 : custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user21 = int(input("enter your choice: "))
    if user21 == 1:
        mycursor.execute("select * from patient")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
    elif user21 == 2:
        mycursor.execute("select pat_name from patient")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user21 == 3:
        mycursor.execute("select pat name,pat_room from patient")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
    elif user21 == 4:
        mycursor.execute("select pat_name,pat_problem from patient")
        headers = mycursor.column_names
    
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user21 == 5:
        custom_query()
    else:
        print("wrong input!!!")

    
def doc_edit():
    print("1 : edit doc_id")
    print("2 : edit doc_name ")
    print("3 : edit doc_sirname")
    print("4 : edit doc_speciality")
    print("5 : edit doc_number")
    print("6: edit doc_email")
    print("7 : edit doc_room")
    print("8: edit doc_salary")
    print("9: custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user12 = int(input("enter your choice: "))
    if user12 == 1:
        udoc_id = input("enter doctor id : ")
        udoc_name = input("enter doctor name: ")
        query = "update doctor set doc id = '{}' where doc name = '{}'".format(udoc_id, udoc_name)
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 2:
        udoc_id = input("enter doctor id :")
        udoc_name = input("enter doctor name: ")
        query = f"update doctor set doc_name = '{udoc_name}' where doc_id = '{udoc_id}'"
        data = mycursor.execute(query)
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 3:
        udoc_id = input("enter doctor id : ")
        udoc_sirname = input("enter doctor sir name: ")
        query = f"update doctor set doc_sirname = '{udoc_sirname}' where doc_id = '{udoc_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 4:
        udoc_id = input("enter doctor id :")
        udoc_speciality = input("enter doctor speciality: ")
        query = f"update doctor set doc_speciality = '{udoc_speciality}' where doc_id = '{udoc_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 5:
        udoc_id = input("enter doctor id :")
        udoc_number = input("enter doctor number: ")
        query = f"update doctor set doc_number = '{udoc_number}' where doc id = '{udoc_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 6:
        udoc_id = input("enter doctor id :")
        udoc_email = input("enter doctor email:")
        query = f"update doctor set doc_email = '{udoc_email}' where doc_id = '{udoc_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 7:
        udoc_id = input("enter doctor id : ")
        udoc_room = int(input("enter doctor room: "))
        query = f"update doctor set doc_room = {udoc_room} where doc_id = '{udoc_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 8:
        udoc_id = input("enter doctor id : ")
        udoc_salary = int(input("enter doctor salary: "))
        query = f"update doctor set doc_salary = {udoc_salary} where doc_id = '{udoc_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 9:
        custom_query()
    else:


        print("wrong input!!!")

    
def pat_edit():
    print("1 : edit patient id")
    print("2: edit patient name ")
    print("3 : edit patient sirname")
    print("4: edit patient problem")
    print("5: edit patient number")
    print("6: edit patient email")
    print("7: edit patient room")
    print("8: custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user22 = int(input("enter your choice: "))
    if user22 == 1:
        upat_id = input("enter patient id : ")
        upat_name = input("enter patient name: ")
        query = f"update patient set pat_id = '{upat_id}' where pat_name = '{upat_name}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user22 == 2:
        upat_id = input("enter patient_id :")
        upat_name = input("enter patient name: ")
        query = f"update patient set pat_name = '{upat_name}' where pat_id = '{upat_id}"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user22 == 3:
        upat_id = input("enter patient_id : ")
        upat_sirname = input("enter patient sir name: ")
        query = f"update patient set pat_sirname = '{upat_sirname}' where pat_id = '{upat_id}'"
    
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        

        else:
            print("done !")
    elif user22 == 4:
        upat_id = input("enter patient id :")
        upat_problem = input("enter patient problem: ")
        query = f"update patient set upat_problem = '{upat_problem}' where pat_id = '{upat_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user22 == 5:
        upat_id = input("enter patient_id : ")
        upat_number = input("enter patient number: ")
        query = f"update patient set pat_number = '{upat_number}' where pat_id = '{upat_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user22 == 6:
        upat_id = input("enter patient_id : ")
        upat_email = input("enter patient email: ")
        query = f"update patient set pat_email = '{upat_email}' where pat_id = '{upat_id}'"
        
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user22==7:
        upat_id = input("enter patient_id : ")
        upat_room = int(input("enter patient room: "))
        query = f"update patient set pat_room = {upat_room} where pat_id = '{upat_id}l'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        
        if not data:
            print("no such data found")
        
        
        
        else:
            print("done !")
    elif user22 *- 8:
        custom_query()
    else:
        print("wrong input!!!")
def doc_change():
    mydb = connection()
    mycursor = mydb.cursor()
    doc_id = input("enter doctor_id : ")
    doctor_name = input("enter doctor name :")
    doc_sirname = input("enter doctor sir name: ")
    doc_speciality = input("enter doctor speciality: ")
    doc_number = input("enter doctor number: ")
    doc_email = input("enter doctor email: ")
    doc_room = int(input("enter doctor room: "))
    doc_salary = int(input("enter doctor salary: "))
    query = f"update doctor set doc_id = '{doc_id}', doc_name = '{doctor_name}', doc_sirname = '{doc_sirname}', doc_speciality = '{doc_speciality}', doc_number = '{doc_number}', doc_email = '{doc_email}', doc_room = {doc_room}, doc_salary {doc_salary} where doc_id = '{doc_id}'"
    
    data = mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    if not data:
        print("no such data found")
    else:
        print("updated Successfully !!")

    
def pat_change():
    mydb = connection()
    mycursor = mydb.cursor()
    pat_id = input("enter patient_id : ")
    patient_name = input("enter patient name :")
    pat_sirname = input("enter patient sir name: ")
    pat_problem = input("enter patient problem: ")
    pat_number = input("enter patient number: ")
    pat_email = input("enter patient email: ")
    pat_room = int(input("enter patient room: "))
    query = f"update patient set pat_id = '{pat_id}', pat_name = '{patient_name}', pat_sirname = '{pat_sirname}', pat_problem = '{pat_problem}', pat_number = '{pat_number}', pat_email = '{pat_email}', pat_room = {pat_room} where pat_id = '{pat_id}'"
    data = mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()

    if not data:
        print("no such data found")
    else:
        print("updated Successfully !I")

    
def view_room():
    print("1 : Full information")
    print("2: view room type")
    print("3 : show available rooms")
    print("4 : custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user41 = int(input("enter your choice: "))
    if user41 == 1:
        query = "select * from room"
        mycursor.execute(query)
        
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers, tablefmt = "psql"))
            print("done !")
    elif user41 == 2:
        query = "select room_assigned_for from room"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers,tablefmt = "psql"))
            print("done !")
    elif user41 == 3:
        query = "select * from room where room_status = 'A'"
        mycursor.execute(query)
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")

        else:
            print(tabulatedata, headers, tablefmt-"psql")
            print("done !")
    elif user41 == 4:
        custom_query()
    else:
        print("wrong input")
def edit_room():
    print("1 : edit room id")
    print("2 : edit room status")
    print("3 : edit room assigned for/room type")
    print("4: edit room capacity")
    print("5 : edit room number")
    print("6: custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user12 = int(input("enter your choice: "))
    if user12 == 1:
        uroom_id = input("enter room id :")
        uroom_no = int(input("enter room number: "))
        query = f"update room set room_id = '{uroom_id}' where room_no = {uroom_no}"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 2:
        uroom_id = input("enter room id : ")
        ustatus = input("enter room status: ")
        query = f"update room set room_status = '{ustatus}' where room_id = '{uroom_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 3:
        uroom_id = input("enter room id :")
        uroom_type = input("enter room type: ")
        query = f"update room set room_assigned_for '{uroom_type}' where room_id = '{uroom_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        if not data:
            print("no such data found")
            
        else:
            print(tabulatedata, headers, tablefmt- "psql")
            print("done !")
    elif user41 ==4:
        custom_query()
    else:
        print("wrong input")
    
    
def edit_room():
    print("1 : edit room id")
    print("2 : edit room status")
    print("3 : edit room assigned for/room type")
    print("4: edit room capacity")
    print("5 : edit room number")
    print("6: custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user12 = int(input("enter your choice: "))
    if user12 == 1:
        uroom_id = input("enter room id :")
        uroom_no = int(input("enter room number: "))
        query = f"update room set room_id = '{uroom_id}' where room_no = {uroom_no}"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 2:
        uroom_id = input("enter room id : ")
        ustatus = input("enter room status: ")
        query = f"update room set room_status = '{ustatus}' where room_id = '{uroom_id}'"
        data =  mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 3:
        uroom_id = input("enter room id :")
        uroom_type = input("enter room type: ")
        query = f"update room set room_assigned_for '{uroom_type}' where room_id = '{uroom_id}'"
        data = mycursor.execute(query)
        mydb.commit()

  
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 * 4:
        uroom_id = input("enter room id :")
        uroom_capacity = int(input("enter room capacity: "))
        query = f"update room set room_capacity = {uroom_capacity} where room id = '{uroom_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 5:
        uroom_id = input("enter room id :")
        uroom_no = int(input("enter room number: "))
        query = f"update room set room_no = {uroom_no} where room_id = '{uroom_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 ==6:
        custom_query()
    else:
        print("wrong input")

        
def change_room():
    mydb = connection()
    mycursor = mydb.cursor()
    uroom_id = input("enter room id : ")
    uroom_status = input("enter room status : ")
    uroom_assigned_for = input("enter room type/room assigned for: ")
    uroom_capacity= int(input("enter room capacity: "))
    
    uroom_no = int(input("enter room number: "))
    query=f"update room set room id = '{uroom_id}', room_status = '{uroom_status}',uroom_assigned_for =  '{uroom_assigned_for}', room_capacity = {uroom_capacity}, room_no = {uroom_no} where room_id = '{uroom_id}'"
    
    data = mycursor.execute(query)
    mydb.commit()
    25

    mycursor.close()
    mydb.close()
    if not data:
        print("no such data found")
    else:
        print("updated Successfully Il")

    
def delete_room():
    mydb = connection()
    mycursor = mydb.cursor()
    uroom_id = input("enter room id : ")
    query =  f"delete from room where room_id = '{uroom_id}'"
    data = mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    if not data:
        print("no such data found")
    else:
        print("deleted Successfully !")

    
def insert_room():
    mydb = connection()
    mycursor = mydb.cursor()
    room_id = input("enter room id : ")
    room_status = input("enter room status :")
    room_assigned_for = input("enter room assigned for/type : ")
    room_capacity = int(input("enter room capacity : "))
    
    room_no = int(input("enter room number"))
    query = f"insert into room values('{room_id}','{room_status}','{room_assigned_for}', {room_capacity}, {room_no})"
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("\nNew room Successfully added!")

    
def add_appointment():
    mydb = connection()
    mycursor = mydb.cursor()
    app_id = input("enter appointment id : ")
    pat_name = input("enter patient name :")
    pat_sirname = input("enter patient sirname :")
    pat_problem = input("enter patient problem :")
    pat_number = input("enter patient number :")
    pat_email = input("enter patient email :")
    doctor = input("enter doctor name :")
    26

    20
    app_date = input("enter appointment date please use this format (YYYY-MM-DD): ")
    app_time = input("enter appointment time please use this format (HH:MM:SS): ")
    query = f"insert into appointment values('{app_id}','{pat_name}','{pat_sirname}', '{pat_problem}', '{pat_number}','{pat_email}','{doctor}', '{app_date}', '{app_time}')"
    mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("\nNew appointment Successfully added!")

           
def view_appointment():
    print("1 : show all appointments")
    print("2 : show appointment id , pat_name and pat_sirname")
    print("3 : show pat problem")
    print("4 : show pat number")
    print("5 : show pat email")
    print("6 : show doctor")
    print("7 : show appointment date")
    print("8 : show appointment time")
    print("9: custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user11 = int(input("enter your choice: "))
    if user11 == 1:
        mycursor.execute("select * from appointment")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 2:
        mycursor.execute("select app_id,pat_name, pat_sirname from appointment")
        headers = mycursor.column_names
        data
        mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers,tablefmt = "psql"))
            print("done !")
    elif user11 == 3:

        mycursor.execute("select pat problem from appointment")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 4:
        mycursor.execute("select pat_number from appointment")
        
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data,headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 5:
        
        mycursor.execute("select pat_email from appointment")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers,tablefmt = "psql"))
            print("done !")
    elif user11 == 6:
        mycursor.execute("select doctor from appointment")
        headers = mycursor.column_names
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 7:
        mycursor.execute("select app date from appointment")
        headers =  mycursor.column_names
        28

        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print(tabulate(data, headers, tablefmt = "psql"))
            print("done !")
    elif user11 == 8:
            mycursor.execute("select app_time from appointment")
            headers = mycursor.column_names
            data = mycursor.fetchall()
            mydb.commit()
            mycursor.close()
            mydb.close()
            if not data:
                print("no such data found")
            else:
                print(tabulate(data,headers, tablefmt = "psql"))
                print("done !")
        
    elif user11 == 9:
            custom_query()
    else:
        print("wrong input!!!")

    
def edit_appointment():
    print("1 : edit appointment id")
    print("2 : edit pat_name and pat_sirname")
    print("3 : edit pat_problem")
    print("4 : edit pat number")
    print("5 : edit pat email")
    print("6 : edit doctor")
    print("7 : edit appointment date")
    print("8 : edit appointment time")
    print("9 : custom query")
    mydb = connection()
    mycursor = mydb.cursor()
    user12 = int(input("enter your choice: "))
    if user12 == 1:
        uapp_id = input("enter appointment id :")
        upat_number = input("enter patient's mobile number :")
        query = f"update appointment set app_id = '{uapp_id}' where pat_number = '{upat_number}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
   

            print("no such data found")
        else:
            print("done !")
    elif user12 == 2:
        uapp_id = input("enter appointment id :")
        upat_name = input("enter patient name: ")
        upat_sirname= input("enter patient sirname: ")
        query = f"update appointment set pat_name = '{upat_name}', pat_sirname = '{upat_sirname}' where app_id {uapp_id}"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 3:
        uapp_id = input("enter appointment id :")
        upat_problem = input("enter patient problem : ")
        query = f"update appointment set pat_problem = '{upat_problem}' where app_id = '{uapp_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 4:
        uapp_id = input("enter appointment id : ")
        upat_number = input("enter patient number :")
        query = f"update appointment set pat_number = '{upat_number}' where app_id = '{uapp_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 5:
        uapp_id = input("enter appointment id :")
        upat_email = input("enter email :")
        query = f"update appointment set pat_email = '{upat_email}' where app_id= '{uapp_id}'"
        data = mycursor.execute(query)
        mydb.commit()

        
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    
    elif user12 == 6:
        uapp_id = input("enter appointment id :")
        udoctor = input("enter doctor name :")
        query = f"update appointment set doctor = '{udoctor}' where app_id = '{uapp_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    
    elif user12 == 7:
        uapp_id = input("enter appointment id : ")
        uapp_date = input("enter appointment date please use this format (YYYY-MM-DD) :")
        query = f"update appointment set app_date = '{uapp_date}' where app_id= '{uapp_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 == 8:
        uapp_id = input("enter appointment id : ")
        uapp_time = input("enter appointment time, please use this format (HH:MM:SS) :")
        query = f"update appointment set app_time = '{uapp_time}' where app_id = '{uapp_id}'"
        data = mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        if not data:
            print("no such data found")
        else:
            print("done !")
    elif user12 ==9:
        custom_query()
    else:
        print("wrong input")
    

def change_appointment():
    mydb - connection()
    mycursor - mydb.cursor()
    uapp_id = input("enter appointment id :")
    upat_name = input("enter patient name :")
    upat_sirname = input("enter patient sirname :")
    upat_problem = input("enter patient problem :")
    upat_number = input("enter patient number :")
    upat_email = input("enter patient email :")
    udoctor = input("enter doctor name : ")
    uapp_date = input("enter appointment date please use this format (YYYY-MM-DD): ")
    uapp_time = input("enter appointment time please use this format (HH:MM:SS) :")
    query = f"update appointment set app_id = '{uapp_id}', pat_name = '{upat_name}', pat_sirname = '{upat_sirname}', pat_problem = '{upat_problem}', pat_number'{upat_number}', pat_email = '{upat_email}', doctor = '{udoctor}', app_date = '{uapp_date}',app_time = '{uapp_time}' where app_id = '{uapp_id}'"
    data = mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    if not data:
        print("no such data found")
    else:
        print("updated Successfully !")


def delete_app():
    mydb = connection()
    mycursor = mydb.cursor()
    uapp_id = input("enter appointment id : ")
    query = f"delete from appointment where app_id = '{uapp_id}'"
    data = mycursor.execute(query)
    mydb.commit()
    mycursor.close()
    mydb.close()
    if not data:
        print("no such data found")
    else:
        print("deleted Successfully !")



