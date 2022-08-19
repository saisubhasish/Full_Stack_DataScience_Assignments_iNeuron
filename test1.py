import csv
import mysql.connector as connection
import logging

mydb = connection.connect(host="localhost", database = 'pandasdb',user="root", passwd="Sai@9556332113",use_pure=True)

print(mydb.is_connected())

query = "CREATE TABLE StudentDetails (Studentid INT(10) AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(60)," \
        "LastName VARCHAR(60), RegistrationDate DATE,Class Varchar(20), Section Varchar(10))"

query4 = "create table if not exists dressSalesDataSet1(`Dress_ID` int,  `29/8/2013` int, `31/8/2013` int, `09/02/2013` int, `09/04/2013` int, `09/06/2013` int, `09/08/2013` int, `09/10/2013` int, `09/12/2013` int, `14/9/2013` int, `16/9/2013` int, `18/9/2013` int, `20/9/2013` int, `22/9/2013` int, `24/9/2013` int, `26/9/2013` int, `28/9/2013` int, `30/9/2013` int, `2013-02-10` int, `2013-04-10` int, `2013-06-10` int, `2010-08-10` int, `10/10/2013` int, `10/12/2013` int)"

cursor = mydb.cursor() #create a cursor to execute queries
cursor.execute(query4)