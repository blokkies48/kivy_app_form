from kivy.uix.screenmanager import Screen

from database.database_jobcards import JobCard, get_job_card, remove_job_card
from database.database import DataBase

class HomeScreen(Screen):
    def test(self):
        print("Home Screen")

    def fab_pressed(self, item):
        self.manager.current = 'JobCardScreen'

    def add_row(self):
        print("Row added")
        new_job_card = JobCard(Title="Job Card 1", Description="Cleaned the toilets", Author="Jonathan")
        new_job_card.add_to_db()

    def remove_row(self):
        print("Row removed")
        remove_job_card()

    def print_rows(self):
        DataBase().connect_to_database()
        sql_query = "SELECT * FROM "