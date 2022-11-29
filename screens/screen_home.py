from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineListItem

from .screen_show_jobcard import LoadJobCard
from database.database_jobcards import JobCard,CreateJobCards, get_all_job_card, remove_job_card, get_c_user_job_card

class HomeScreen(Screen):
    # Add more tabs here
    # Tabs variables
    active_tab = "Job Cards"

    # App variables
    current_user = ""

    user_card = []

    def __init__(self, **kw):
        super().__init__(**kw)
        CreateJobCards().job_card_table()
    
    # Add more tabs here
    def fab_pressed(self):
        if self.active_tab == "Job Cards":
            self.manager.current = 'JobCardScreen'
            
        if self.active_tab == "Test Cards":
            print("You are on the test tab")
            print(self.active_tab)

            
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
            for index, name in enumerate(get_c_user_job_card(self.current_user)):
                
                widget = TwoLineListItem(
                    text=f"{index + 1}: {name[1]}",
                    secondary_text=f"Date Created: {name[2][:10]}" ,
                    on_release=self.open_form
                )
                self.ids.home_dis.add_widget(widget)

                self.user_card.append((index + 1,name))
                
        except:
            print("error")

    def open_form(self, data):
        
        self.manager.current = 'LoadJobCard'
        self.manager.transition.direction = 'left'
        
        with open("user//current_form.txt", "w") as f:
            for i in self.user_card:
                if (int(data.text.split(": ")[0]) == int(i[0]) 
                    and data.text.split(": ")[1] == i[1][1]):
                    for details in i[1]:
                        f.write(f"{details}\n")
            self.user_card =[]
                

      

    def remove_content(self):
        self.ids.home_dis.clear_widgets()
        self.user_card = []


    