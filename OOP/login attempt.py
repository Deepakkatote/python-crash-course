class user:
    def __init__(self, first_name, last_name,username,email,location,role):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.role = role
        self.login_attempt = 0
        pass
    
    def describe(self):
        long_name = f"{self.first_name}{self.last_name}\n{self.username}\n{self.email}\n{self.location}\n{self.role}"
        return long_name
    
    def greet_user(self):
        print(f"Welcome back {self.first_name}")

    def increment_login_attempt(self,attempt):
        self.login_attempt += attempt
    
    def login_reset(self):
        self.login_attempt = 0
   

Dhruvi = user("Dhruvi","Krushna","dhruviK","dhruvi.k@dingding.in","Tokyo","Super User")
print(Dhruvi.describe())
print("\n")
Dhruvi.greet_user()
print("\nMaking three login attempt")
Dhruvi.increment_login_attempt(1)
Dhruvi.increment_login_attempt(1)
Dhruvi.increment_login_attempt(1)
print("\nResetting login attempts...")
Dhruvi.login_reset()
print(f"Login reset {Dhruvi.login_attempt}")