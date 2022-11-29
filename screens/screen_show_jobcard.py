
# Add option to delete or to edit

from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

class LoadJobCard(Screen):
 
    def load_card(self):
        labels = ["Title", "Date and Time", "Description", "Author"]
        with open("user//current_form.txt", "r") as f:
            next(f)
            for index, line in enumerate(f):
                widget = MDLabel(
                    text = f"{labels[index]}:\n {line}",
                    halign = 'center'
                )
                self.ids.boxlayout.add_widget(widget)

    def cancel(self):
        with open("user//current_form.txt", "w") as f:
            f.write('')
        self.ids.boxlayout.clear_widgets()
        self.manager.current = 'HomeScreen'
        self.manager.transition.direction = 'right'

       