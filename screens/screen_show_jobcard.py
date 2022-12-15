
# Add option to edit
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from database.database_jobcards import remove_job_card

class LoadJobCard(Screen):
 
    def load_card(self):
        labels = ["Title", "Date and Time", "Description", "Author"]
        with open("user//current_form.csv", "r") as f:
            next(f)
            for index, line in enumerate(f):
                widget = MDLabel(
                    text = f"{labels[index]}:\n {line}",
                    halign = 'center'
                )
                self.ids.boxlayout.add_widget(widget)

    def cancel(self):
        with open("user//current_form.csv", "w") as f:
            f.write('')
        self.ids.boxlayout.clear_widgets()
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'

    def delete(self):
        id = None
        title = ""

        with open("user//current_form.csv", "r") as f:
            for index, line in enumerate(f):
                print(index)
                if index == 0:
                    id = int(line)
                elif index == 1:
                    title = line.strip("\n")
                
        if id != None:
            remove_job_card(id=id, job_card_title=title)
            self.cancel()
        else:
            print("Unable to delete")
            self.cancel()

    