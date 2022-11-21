from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.screen_home import HomeScreen
from screens.screen_login import LoginScreen
from screens.screen_jobcard import JobCardScreen

THEME_ = "Dark"

class MainApp(MDApp):
    def theme_(self):
        self.theme_cls.theme_style = THEME_
        self.theme_cls.primary_palette = "DeepOrange"

    def build(self):
        self.theme_()
        Builder.load_file("design.kv")
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(name = "LoginScreen"))
        screen_manager.add_widget(HomeScreen(name = "HomeScreen"))
        screen_manager.add_widget(JobCardScreen(name = "JobCardScreen"))
        return screen_manager


    
    

    
if __name__ == "__main__":

    MainApp().run()