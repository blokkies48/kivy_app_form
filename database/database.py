import mysql.connector

PASSWORD = ''

class DataBase():
    def __init__(self):
        db = mysql.connector.connect(
            host= "localhost", # 
            user="root", # 
            passwd = PASSWORD, #
        )

        cursor = db.cursor(buffered=True)

        cursor.execute("CREATE DATABASE IF NOT EXISTS dev_database")

        db.commit()
    def connect_to_database(self):
            return mysql.connector.connect(
            host= "localhost", # 
            user="root", # 
            passwd = PASSWORD, #
            database = "dev_database" # 
        )
    