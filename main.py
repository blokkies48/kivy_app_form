from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

error_occurred = False
try:
    from screens.screen_login import LoginScreen
    from screens.screen_home import HomeScreen
    from screens.screen_register import RegisterScreen
    from screens.screen_jobcard import JobCardScreen
    from screens.screen_show_jobcard import LoadJobCard
except Exception as e:
    from screens.screen_error_screen import ErrorScreen
    error_occurred = True
    error_message = e

THEME_ = "Dark"
THEME_PALETTE = "DeepOrange"

class MainApp(MDApp):
    def theme_(self):
        self.theme_cls.theme_style = THEME_
        self.theme_cls.primary_palette = THEME_PALETTE

    def build(self):
        self.theme_()
        Builder.load_file("design.kv")
        screen_manager = ScreenManager()
        if not error_occurred:
            screen_manager.add_widget(LoginScreen(name = "LoginScreen"))
            screen_manager.add_widget(RegisterScreen(name = "RegisterScreen"))
            screen_manager.add_widget(HomeScreen(name = "HomeScreen"))
            screen_manager.add_widget(JobCardScreen(name = "JobCardScreen"))
            screen_manager.add_widget(LoadJobCard(name = "LoadJobCard"))

        else:
            screen_manager.add_widget(ErrorScreen(
                name = "ErrorScreen", 
                error_type=error_message,
                ))
        return screen_manager


if __name__ == "__main__":
    try:
        MainApp().run()
    except Exception as e:
        print("Main ",e)
