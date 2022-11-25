from kivy.uix.screenmanager import Screen
from database.database_jobcards import JobCard
from kivy.clock import Clock
from datetime import date, datetime


class JobCardScreen(Screen):
    def test(self):
        print("Login screen")


    def add_job_card(self, title, description):
        with open("user//user.txt", "r") as f:
            for index, line in enumerate(f):
                    if index == 0:
                        user = (line.split()[-1])
        if title.text != '' and description.text != '':               
            new_job_card = JobCard(Title=title.text, Description=description.text, Author=user)
            new_job_card.add_to_db()
            title.text = ''
            description.text = ''
            
            self.manager.current = 'HomeScreen'
            self.manager.transition.direction = 'right'
        else:
            title.required = True
            description.required = True
            self.ids.error.text = "No empty fields allowed"
            Clock.schedule_once(self.remove_error, 3)

    def display_date(self, _date):
        current_time = datetime.now().strftime("%H:%M:%S")
        _date.text = "Date: " + str(date.today()) + " Time: " + str(current_time)
        
    def remove_error(self, *args):
        print(args)
        self.ids.error.text = ""

    def back(self):
        self.ids.title.text = ''
        self.ids.description.text = ''
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'