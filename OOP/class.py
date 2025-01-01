class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurat(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")
        

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")


obj1 = restaurant("The family place", "Pure Veg")
obj1.describe_restaurat()
obj1.open_restaurant()
print("\n")
obj2 = restaurant("Friends", "Non-veg")
obj2.describe_restaurat()
obj2.open_restaurant()
print("\n")
obj3 = restaurant("Paradise", "Beer cafe")
obj3.describe_restaurat()
obj3.open_restaurant()
print("\n")
class user:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.location = "Tokyo"
        self.skill = "Python"

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.location} {self.skill}")

    def greet_user(self):
        print(f"Hi {self.first_name} welcome to {self.skill} crash course")

u1 = user("Dhruvi", "Krushna")
u1.describe_user()
u1.greet_user()

u2 = user("Deepak", "K")
u2.describe_user()
u2.greet_user()

u3 = user("CS", "K")
u3.describe_user()
u3.greet_user()
