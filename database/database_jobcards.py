from .database import  DB, CURSOR
from datetime import datetime


class CreateJobCards():
    def job_card_table(self):
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS job_card_table 
            (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(50),
            time Text,
            description VARCHAR(240),
            author VARCHAR(50)
            )
        """)

        DB.commit()

class JobCard():

    def __init__(self, Title, Author, Description):
        self.Time = datetime.today()
        self.Title = Title
        self.Description = Description
        self.Author = Author

    # Tuple needed to add to database
    def add_to_db(self):
        CreateJobCards().job_card_table()
        sql_command = "INSERT INTO job_card_table (time,title,description,author) VALUES (%s,%s,%s,%s) "
        content = (self.Time, self.Title, self.Description, self.Author)
        CURSOR.execute(sql_command, content)
        DB.commit()

# Edit later
def remove_job_card():
    sql_command = "DELETE FROM job_card_table LIMIT 1 "
    CURSOR.execute(sql_command)
    DB.commit()

# prints all cards for testing
def get_all_job_card():
    sql_command = "SELECT * FROM job_card_table"
    CURSOR.execute(sql_command)
    result = CURSOR.fetchall()
    for row in result:
        print(row,"\n")

# Returns list of current logged in user's job cards
def get_c_user_job_card(username):
    job_cards_list = []
    sql_command = f"SELECT * FROM job_card_table WHERE author = '{username}'"
    CURSOR.execute(sql_command)
    result = CURSOR.fetchall()
    for row in result:
        job_cards_list.append(row)
    return job_cards_list


    