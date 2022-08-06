import csv
import pandas as pd
import os
import mysql.connector as conn
import mysql.connector as connection
import logging

'''
    This is logging function to create a file to store program execution result
'''
logging.basicConfig(filename='Task.log', level=logging.INFO)


try:
    """
        This is the program to create a table
    """
    mydb = connection.connect(host="localhost",user="root", passwd="Sai@9556332113",use_pure=True,database='pandasdb')
    cursor = mydb.cursor()
    query1 = 'create database pandasdb'
    # cursor.execute(query1)
    query2 = "create table if not exists pandasdb.attributeDataSet(Dress_ID int, Style varchar(20), Price varchar(10), ' \
             'Rating float(4), Size varchar(20), Season varchar(20), NeckLine varchar(20), SleeveLength varchar(20), ' \
             'waiseline varchar(20),Material varchar(20), FabricType varchar(20), Decoration varchar(20), ' \
             'PatternType varchar(20), Recommendation int)"

    query3 = "LOAD DATA INFILE 'D:/FSDS-iNeuron/3.Resource/dataFSDS/AttributeDataSet.csv' INTO TABLE pandasdb.attributeDataSet FIELDS TERMINATED BY ','"

    query4 = "create table if not exists dressSalesDataSet(`Dress_ID` int,  `29/8/2013` int, `31/8/2013` int, `09/02/2013` int, `09/04/2013` int, `09/06/2013` int, `09/08/2013` int, `09/10/2013` int, `09/12/2013` int, `14/9/2013` int, `16/9/2013` int, `18/9/2013` int, `20/9/2013` int, `22/9/2013` int, `24/9/2013` int, `26/9/2013` int, `28/9/2013` int, `30/9/2013` int, `2013-02-10` int, `2013-04-10` int, `2013-06-10` int, `2010-08-10` int, `10/10/2013` int, `10/12/2013` int)"

    query5 = "LOAD DATA INFILE 'D:/FSDS-iNeuron/3.Resource/dataFSDSDressSales.csv' INTO TABLE pandasdb.dressSalesDataSet FIELDS TERMINATED BY ','"

    cursor.execute(query5)
    cursor.commit()




    print('FSDS')














except Exception as e:
    logging.exception(e)

















#query = "show databases"
#cursor = mydb.cursor() #create a cursor to execute queries
#s = cursor.execute(query)
#print(s)
#print("Database Created!!")
#mydb.close()

#query1 = "create table attributeDateSet(Dress_ID int, )"