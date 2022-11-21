from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from screens.screen_home import HomeScreen
from database.database_jobcards import CreateJobCards



class MainApp(MDApp):
    def theme_(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"

    def build(self):
        self.theme_()
        Builder.load_file("design.kv")
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name = "HomeScreen"))
        return screen_manager

    
def main():
    CreateJobCards.job_card_table()
    
if __name__ == "__main__":
    main()
    MainApp().run()