from kivy.uix.screenmanager import Screen
from database.database_user import all_users, single_user
from kivy.clock import Clock

from kivy.uix.screenmanager import NoTransition, SlideTransition


class LoginScreen(Screen):
    # TODO: figure out encryption method with key
    def encrypt_password(self, password: str):
        return str(password) + "1"
        
    # TODO:
    def decrypt_password(self, password: str):
        return str(password).rstrip("1")

    user_ids = []
    target = 0
    def login(self, user_name,user_password):
        try:
            user = single_user(user_name.text)
            if user[1] == user_name.text.lower().capitalize() and user[2] == user_password.text:
                # Save user login
                with open("user//user.txt", "w+") as f:
                    f.write(f"User: {user[1]}\nid: {user[0]}\npassword: {self.encrypt_password(user[2])}")
                # Clear inputs
                self.ids.login_error.text = ''
                user_name.text = ''
                user_password.text = ''
                # Change screen
                self.manager.current = 'HomeScreen'
                self.manager.transition.direction = 'left'
            else:
                raise Exception()
        except Exception as e: 
            print(e)
            self.ids.login_error.text = "Invalid username or password"
            user_password.text = ''
            # Time error message to go away
            Clock.schedule_once(self.update_label, 2)

        print(all_users())


    def update_label(self, *args):
        self.ids.login_error.text = ''

    # Checks if their is a logged in user
    def check_login(self):
        Clock.schedule_once(self.pre_login, 0.1)
    def pre_login(self, *args):
        try:
            with open("user//user.txt", "r") as f:
                for index, line in enumerate(f):
                    if index == 0:
                        user = single_user(line.split()[-1])
                    if index == 1:
                        id = line.split()[-1]
                    if index == 2:
                        password = self.decrypt_password(line.split()[-1]) 
                    
            user_id = user[0]
            user_name = user[1]
            user_password = self.decrypt_password(user[2])

            if ((user[1]) == (user_name)) and ((user_password) == (password)) and ((id) == str(user_id)):
                self.manager.transition = NoTransition()
                self.manager.current = 'HomeScreen'
                self.manager.transition = SlideTransition()
            else:
                raise Exception()
        except:
            with open("user//user.txt", "w") as f:
                f.write('')  

    # REMOVE     
    # Uses binary search to find user
    def binary_search(self): 
        left = 0 
        right = len(self.user_ids) - 1 

        while left <= right: 
            mid = (right + left) // 2 
            if self.user_ids[mid] == self.target: 
                return mid # index of user
            elif self.user_ids[mid] < self.target: 
                left = mid + 1 
            else:
                right = mid - 1 
        return - 1


    # Get logged in user setting from json file