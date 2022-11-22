from kivy.uix.screenmanager import Screen
from database.database_user import all_users
from kivy.clock import Clock

from kivy.uix.screenmanager import NoTransition, SlideTransition


class LoginScreen(Screen):
    user_ids = []
    target = 0
    def login(self, user_name,user_password):
        try:
            for user in all_users():
                if user[1] == user_name.text.lower().capitalize() and user[2] == user_password.text:
                    # Change screen
                    self.manager.current = 'HomeScreen'
                    self.manager.transition.direction = 'left'
                    # Set user name and id
                    # use a text document for simplicity
                    with open("user//user.txt", "w+") as f:
                        f.write(f"User: {user[1]}\nid: {user[0]}")
                    # Clean out text inputs
                    self.ids.login_error.text = ''
                    user_name.text = ''
                    user_password.text = ''
                    break
            else:
                self.ids.login_error.text = "Invalid username or password"
                user_name.text = ''
                # Time error message to go away
                Clock.schedule_once(self.update_label, 2)
        except Exception as e:
            print(e)
            self.ids.login_error.text = "Error occurred contact admin"

        print(all_users())


    def update_label(self, *args):
        self.ids.login_error.text = ''

    # Checks if their is a logged in user
    def check_login(self):
        Clock.schedule_once(self.pre_login, 0.1)
    def pre_login(self, *args):
        self.user_ids = [int(user[0]) for user in all_users()]
        with open("user//user.txt", "r") as f:
            for line in f: # Loop because max 2 lines and small scalable
                if "id" in line:
                    # Sets the target for the search
                    self.target = int(line.split()[-1])
                    user_index = self.binary_search()
                    # Getting the name and password 
                    self.ids.user_name.text = all_users()[user_index][1]
                    self.ids.user_password.text = all_users()[user_index][2]
                    self.manager.transition = NoTransition()
                    self.manager.current = 'HomeScreen'
                    self.manager.transition = SlideTransition()
                    print(all_users()[user_index][1],all_users()[user_index][2])
                    break
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
