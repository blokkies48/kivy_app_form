from database.database_user import AddUser
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


class RegisterScreen(Screen):
    def register_user(self, name, password, password_2, error):
        try:
            if name.text != "" and password.text != "":
                if password.text == password_2.text:
                    AddUser(
                        name.text.lower().capitalize(),
                        password.text).register_user()
                    name.text = ''
                    password.text = ''
                    password_2.text = ''
                    self.manager.current = 'LoginScreen'
                    self.manager.transition.direction = 'left'
                else:
                    error.text = "Passwords do not match"
                    password.text = ''
                    Clock.schedule_once(self.update_label, 2)
            else: 
                error.text = "Can't have empty fields" 
                Clock.schedule_once(self.update_label, 2)
        except Exception as e:
            print(e)
            password.text = ''
            password_2.text = ''
            error.text = 'Invalid username or password'
            Clock.schedule_once(self.update_label, 2)

    def update_label(self, *args):
        self.ids.login_error.text = ''