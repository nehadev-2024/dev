# Assignment – Software Engineer Trainee
This project demonstrates my proficiency in Python Flask, MySQL, and Git by implementing a simple API with database interactions.
### 🚀 Prerequisites
Before running this application ensure you have installed these dependencies
- Python 3.x
- Flask (`pip install flask`)
- MySQL
- Git
### ✅ Installation and Setup
1. Clone the Repository

   git clone https://github.com/nehadev-2024/dev.git  
   cd repository-name
   
2. Install Dependencies  
   pip install -r requirements.txt
3. *Database Setup*    
   Run the following SQL commands to set up the database:  

   *CREATE DATABASE users;*    
   
   *CREATE TABLE users (*  
       id INT AUTO_INCREMENT PRIMARY KEY,    
       name VARCHAR(30),    
       email VARCHAR(30)    
   *);*

4. Populate the table with sample data

🗄️ Database Interection

:diamond_shape_with_a_dot_inside:  Create Database 
create database users;
:diamond_shape_with_a_dot_inside: switch database
use users;
create table users(id int primary key, name varchar(30), email varchar(30), role varchar(30));
insert into users(id,name,email,role) values(101,'Neha','neha@gmail.com','software developer');
select * from users;
select * from users where id=101; 


     

