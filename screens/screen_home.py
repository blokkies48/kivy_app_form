from kivy.uix.screenmanager import Screen
from database.database import DataBase

from database.database_jobcards import JobCard, RemoveJobCard

class HomeScreen(Screen):
    def test(self):
        print("Home Screen")

    def fab_pressed(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        # cursor.execute("SELECT * FROM job_card_table")
        cursor.execute("SELECT * FROM job_card_table")

        result = cursor.fetchall()
        print()
        for i in result:
            
            print(i)

    def add_job_card(self):
        new_job_card = JobCard(Title="Job Card 1", Description="Cleaned the toilets", Author="Jonathan")
        new_job_card.add_to_db()

    def remove_job_card(self):
        RemoveJobCard().remove_job_card()