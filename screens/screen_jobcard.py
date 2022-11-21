from kivy.uix.screenmanager import Screen
from database.database_jobcards import JobCard, get_job_card, remove_job_card

class JobCardScreen(Screen):
    def test(self):
        print("Login screen")


    def add_job_card(self):
        new_job_card = JobCard(Title="Job Card 1", Description="Cleaned the toilets", Author="Jonathan")
        new_job_card.add_to_db()

    def remove_job_card(self):
        remove_job_card()


    def back(self):
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'