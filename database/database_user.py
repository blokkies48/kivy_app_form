from .database import  DB, CURSOR

class UserTable:
    def create_user_table(self):
        sql_command = """CREATE TABLE IF NOT EXISTS users
        (
        id INTEGER AUTO_INCREMENT,
        username VARCHAR(50),
        password VARCHAR(50),
        primary key (id, username)   
        )"""
        CURSOR.execute(sql_command)
        DB.commit()

class AddUser:

    def __init__(self, username, password):
    
        self.username = username
        self.password = password

    def register_user(self):
        UserTable().create_user_table()
        sql_command = "INSERT INTO users (username, password) VALUES (%s, %s)"
        content = (self.username, self.password)
        CURSOR.execute(sql_command, content)
        DB.commit()

def all_users():
    CURSOR.execute("SELECT * FROM users")
    return [users for users in CURSOR.fetchall()]

def single_user(username1):
    CURSOR.execute(f"SELECT * FROM users WHERE username = '{username1}'" )
    return CURSOR.fetchone()