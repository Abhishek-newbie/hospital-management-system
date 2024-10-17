
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


*  *Install **tabulate module** It is used to display structured date same as data shown in mysql*

    ```
    pip install tabulate
    
    ``` 
    
    
* Run the followings commands in mysql command line interface , You will also be given a mysql file
```
  create database if not exists hospital;

  create table if not exists doctor(doc_id varchar(4), doc_name varchar(10), doc_sirname varchar(10), doc_speciality varchar(10), doc_number varchar(10), doc_email varchar(20), doc_room int(3), doc_salary int (5));

  create table if not exists patient(pat_id varchar(4), pat_name varchar(10), pat_sirname varchar(10), pat_problem varchar(10), pat_number varchar(10), pat_email varchar(20), pat_room int(3));

  create table if not exists room (room_id varchar(4), room_status char(1), room_assigned_for varchar(10), room_capacity int(3), room_no int(3));

  create table if not exists appointment (app_id varchar(4), pat_name varchar(10), pat_sirname varchar(10), pat_problem varchar(10), pat_number varchar(10), pat_email varchar(10), doctor varchar(10), app_date date, app_time time);
```

## Tips & Issues

* If pip is not working just go for online solutions **(try to run the cmd in administor mode or add pip to the environment vairables)**
* While installing python make sure to check the "add to path" check box 
* Delete old versions of python if any issue happens

* There are some minor bugs they will soon sorted out 
* You can even change or add the database creation or add command like "if not exists" in connection function in main_functions module 
* keep both the main_funtions & main.py in the same directory


## Video

https://user-images.githubusercontent.com/68725300/178411614-ebdf0141-8ba2-4f7d-957d-1e60fc88d22a.mp4


## Screenshots

![App Screenshot 1](https://drive.google.com/uc?id=12KckuyOgSBHzNuiTjwC-xcyUx3tlwZdP)

![App Screenshot 2](https://drive.google.com/uc?id=1Kpba2245WfGz3shsOSHtd1bCvqryQMRC)

![App Screenshot 3](https://drive.google.com/uc?id=1B0BKQKyuUgKPuLF5T6xRMAWpRBWxSTz7)

![App Screenshot 4](https://drive.google.com/uc?id=1fS1X1HVp8KsiMIzc1TN2CwAs9BWMe9Rm)

![App Screenshot 5](https://drive.google.com/uc?id=1l4y-K-9UY1pmG1vLFhoMR7aBM69YNW_x)

![App Screenshot 6](https://drive.google.com/uc?id=1aVjGcv6pwN_7sOqZnPkqazbMG1YSkTlV)

![App Screenshot 7](https://drive.google.com/uc?id=1GlqRGZBuV7-xxIkD0sAgJidMhdRoux-x)

![App Screenshot 8](https://drive.google.com/uc?id=14en8jW2qS9-FydGl9jP0aRfNbJi17ckc)

![App Screenshot 9](https://drive.google.com/uc?id=1pKIZJfgEMkpuwkRhFTr60tSWYXG9wuf8)

![App Screenshot 10](https://drive.google.com/uc?id=1XZJZ89DT6WJithAa49dvPh4q2RuMsIU1)

![App Screenshot 11](https://drive.google.com/uc?id=16NP5rX4CaXV1TOygJK6_neznNT-vq5qC)

![App Screenshot 12](https://drive.google.com/uc?id=19zyeqYuA_7SPbd_dywlx5NOHEJodb2k5)

![App Screenshot 13](https://drive.google.com/uc?id=1CO21akl7NT3385Drs2uzajSgZwiayNPs)

![App Screenshot 14](https://drive.google.com/uc?id=1gdNpIP5jZvNc5sYwDiHF1rBRHQL7jqtS)





## license

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Support

For support, email ak0188644@gmail.com.

