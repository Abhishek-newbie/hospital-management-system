#hospital management system
A simple school level project

how to run the program

1 install mysql-connector-python module from pypi just run this command "pip install mysql-connector-python" in cmd (without quotes)
2 install tabulate module using "pip install tabulate" in cmd (without quotes it is used to display structured date like data shown in mysql)
3 run the followings commands in mysql you will also be given mysql file 
4 you are all set just run the hospital management main.py file keep both python files (hospital management main.py and main_functions) in the same directory

* if pip is not working just go for online solution (try to run the cmd in administor mode)
* don't forget to share your comment or give your feedbacks
* there are some minor bugs there they will soon sorted out 
* you can even change or add the database creation if not exists in connection function in main_function module   


 		mysql 
create database if not exists hospital

create table if not exists doctor(doc_id varchar(4), doc_name varchar(10), doc_sirname varchar(10), doc_speciality varchar(10), doc_number varchar(10), doc_email varchar(20), doc_room int(3), doc_salary int (5))

create table if not exists patient(pat_id varchar(4), pat_name varchar(10), pat_sirname varchar(10), pat_problem varchar(10), pat_number varchar(10), pat_email varchar(20), pat_room int(3))

create table if not exists room (room_id varchar(4), room_status char(1), room_assigned_for varchar(10), room_capacity int(3), room_no int(3))

create table if not exists appointment (app_id varchar(4), pat_name varchar(10), pat_sirname varchar(10), pat_problem varchar(10), pat_number varchar(10), pat_email varchar(10), doctor varchar(10), app_date date, app_time time)
