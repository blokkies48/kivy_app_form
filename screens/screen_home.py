from kivy.uix.screenmanager import Screen
from database.database_user import all_users
from screens.screen_login import LoginScreen

from database.database_jobcards import JobCard, get_job_card, remove_job_card

class HomeScreen(Screen):
    # functions for testing purposes
    def test(self):
        print("Home Screen")

    def add_row(self):
        print("Row added")
        new_job_card = JobCard(Title="Job Card 1", Description="Cleaned the toilets", Author="Jonathan")
        new_job_card.add_to_db()

    def remove_row(self):
        print("Row removed")
        remove_job_card()

    def print_rows(self):
        get_job_card()
##################################################
    # Add more tabs here
    # Tabs variables
    active_tab = "Job Cards"

    # App variables
    current_user = ''

    def fab_pressed(self):
        if self.active_tab == "Job Cards":
            self.manager.current = 'JobCardScreen'

    def current_tab(self, tab):
        self.active_tab = tab.name

    def set_user(self,hello_bar):
        with open("user//user.txt", "r") as f:
            for line in f:
                if "User" in line:
                    hello_bar.title = f"Hi, {line.split()[-1]}"

    def logout(self):
        with open("user//user.txt", "w+") as f:
            f.write('')
        self.manager.current = 'LoginScreen'
        self.manager.transition.direction = 'right'



    