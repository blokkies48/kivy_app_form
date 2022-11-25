from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineListItem


from database.database_jobcards import JobCard,CreateJobCards, get_all_job_card, remove_job_card, get_c_user_job_card

class HomeScreen(Screen):
    # Add more tabs here
    # Tabs variables
    active_tab = "Job Cards"

    # App variables
    current_user = ""

    def __init__(self, **kw):
        super().__init__(**kw)
        CreateJobCards().job_card_table()
    # functions for testing purposes
    
    def add_row(self):
        print("Row added")
        new_job_card = JobCard(Title="Job Card 1", Description="Cleaned the toilets", Author="Jonathan")
        new_job_card.add_to_db()

    def remove_row(self):
        print("Row removed")
        remove_job_card()

    def print_rows(self):
        get_all_job_card()
##################################################
    

    def fab_pressed(self):
        if self.active_tab == "Job Cards":
            self.manager.current = 'JobCardScreen'

            
    def current_tab(self, tab):
        self.active_tab = tab.name

    def set_user(self,hello_bar):
        with open("user//user.txt", "r") as f:
            for line in f:
                if "User" in line:
                    self.current_user = line.split()[-1]
                    hello_bar.title = f"Hi, {line.split()[-1]}"

    def logout(self):
        with open("user//user.txt", "w+") as f:
            f.write('')
        self.manager.current = 'LoginScreen'
        self.manager.transition.direction = 'right'


    def load_content(self):
        try:
            # print(get_c_user_job_card(self.current_user)) # list of job cards
            for name in get_c_user_job_card(self.current_user):
                widget = TwoLineListItem(
                    text=f"Title: {name[1]} Description: {name[3][:15]}...",
                    secondary_text=f"Date Created: {name[2][:10]}" ,
                    on_release=lambda _: self.open_form(name)
                )
                self.ids.home_dis.add_widget(widget)
        except:
            print("error")

    def open_form(self, name):
        print(name)


    def remove_content(self):
        self.ids.home_dis.clear_widgets()


    