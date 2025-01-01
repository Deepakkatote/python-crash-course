class User:
    def __init__(self,first_name,last_name,usename,email,location):
        self.first_name = first_name
        self.last_name =last_name
        self.username = usename
        self.email = email
        self.location = location
    def describe(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"username: {self.username}")
        print(f"email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome back {self.first_name}")
    
class Admin(User): # type: ignore
    def __init__(self,first_name,last_name,usename,email,location):
        super().__init__(first_name,last_name,usename,email,location)
        self.privileage = privileage()
        
class privileage:
    def __init__(self,privileage):
        self.privileage = privileage

    def show_privileage(self):
        privileage = f"{self.privileage} can add post","can delete post","can ban user"
        return privileage
    
dhruvi = Admin("Dhruvi","Arulkar","dhruviA","dhruvi.a@abc.in","Tokyo")
dhruvi.describe()
dhruvi.greet_user()
dhruvi.privileage = f"{dhruvi.privileage}: super user","can add post","can delete post","can ban user"
print(dhruvi.show_privileage())

deepak = Admin("Deepak", "Katote","deepakK","deepak.k@abc.in","Tokyo")
deepak.describe()
deepak.greet_user()
print(deepak.show_privileage())