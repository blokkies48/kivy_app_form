import mysql.connector

PASSWORD = 'Jlloyd15'

class DataBase():
    def __init__(self):
        # To connect to create database
        db = mysql.connector.connect(
            host= "localhost", # 
            user="root", # 
            passwd = PASSWORD, #
        )
        cursor = db.cursor(buffered=True)
        cursor.execute("CREATE DATABASE IF NOT EXISTS dev_database")
        db.commit()
        db.close()


    # Connects after database has been created
    def connect_to_database(self):
        return mysql.connector.connect(
        host= "localhost", # 
        user="root", # 
        passwd = PASSWORD, #
        database = "dev_database" # 
        )
          

DB = DataBase().connect_to_database()
CURSOR = DB.cursor(buffered=True)


