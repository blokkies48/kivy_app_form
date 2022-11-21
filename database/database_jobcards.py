from .database import DataBase
from random import randint
from datetime import date

DB = DataBase().connect_to_database()
CURSOR = DB.cursor(buffered=True)

class CreateJobCards():
    def job_card_table():
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS job_card_table 
            (
            id INTEGER PRIMARY KEY,
            title VARCHAR(50),
            time DATETIME,
            description VARCHAR(240),
            author VARCHAR(50)
            )
        """)

        DB.commit()

class JobCard():

    def __init__(self, Title, Author, Description):
        self.Id = randint(1000,9999)
        self.Time = date.today()
        self.Title = Title
        self.Description = Description
        self.Author = Author

    # Tuple needed to add to database
    def add_to_db(self):
        sql_command = "INSERT INTO job_card_table (id,time,title,description,author) VALUES (%s,%s,%s,%s,%s) "
        content = (self.Id, self.Title, self.Description, self.Author)
        CURSOR.execute(sql_command, content)
        DB.commit()


def remove_job_card(self):
    sql_command = "DELETE FROM job_card_table LIMIT 1 "
    CURSOR.execute(sql_command)
    DB.commit()


def get_job_card(self):
    sql_command = "SELECT * FROM job_card_table"
    CURSOR.execute(sql_command)
    DB.commit()

    