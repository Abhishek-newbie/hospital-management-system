
# HOSPITAL MANAGEMENT SYSTEM

A simple school level project, Developed with PYTHON
integrated with MYSQL database management system 


## Files

 - [main.py](https://github.com/coder-abhi07/hospital-management-system/blob/main/hospital%20management%20system/hospital%20management%20main.py)
 - [main_functions.py](https://github.com/coder-abhi07/hospital-management-system/blob/main/hospital%20management%20system/main_functions.py)
 - [mysql.sql](https://github.com/coder-abhi07/hospital-management-system/blob/main/hospital%20management%20system/mysql.sql)


## Features

- Mysql integrated with python
- All exceptions are handled
- Easy user interface
- Result shown are same as data shown in mysql 


## How To Run The Project
HOW TO RUN THE PROJECT 

**Run these commands in cmd**
*  *Install **mysql connector module** used to connect mysql with python*

    ```
    pip install mysql-connector-python
    
    ``` 


*  *Install **tabulate module** using It is used to display structured date like data shown in mysql*

    ```
    pip install tabulate
    
    ``` 
    
    
* Run the followings commands in mysql you will also be given mysql file
```
  create database if not exists hospital;

  create table if not exists doctor(doc_id varchar(4), doc_name varchar(10), doc_sirname varchar(10), doc_speciality varchar(10), doc_number varchar(10), doc_email varchar(20), doc_room int(3), doc_salary int (5));

  create table if not exists patient(pat_id varchar(4), pat_name varchar(10), pat_sirname varchar(10), pat_problem varchar(10), pat_number varchar(10), pat_email varchar(20), pat_room int(3));

  create table if not exists room (room_id varchar(4), room_status char(1), room_assigned_for varchar(10), room_capacity int(3), room_no int(3));

  create table if not exists appointment (app_id varchar(4), pat_name varchar(10), pat_sirname varchar(10), pat_problem varchar(10), pat_number varchar(10), pat_email varchar(10), doctor varchar(10), app_date date, app_time time);
```

## Tips & Issues

* If pip is not working just go for online solution **(try to run the cmd in administor mode or add pip to the environment vairables)**
* Delete old versions of python if any issue happens

* There are some minor bugs there they will soon sorted out 
* You can even change or add the database creation if not exists in connection function in main_function module  

## license

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Support

For support, email ak0188644@gmail.com.

