class restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def describe(self):
        long_name = f"{self.name} {self.cuisine}"
        return long_name
    
    def current_customer(self):
        print(f"{self.served}")

    def cust_served(self,customer):
        self.served = customer
        print(f"{self.name} has served {self.served} customer today")
    
    def incriment(self,customer):
        self.served += customer
        print(f"{self.name} has srved {self.served} customer today")


obj1 = restaurant("Paradise", "Pure Veg")
print(obj1.describe())
obj1.current_customer()
obj1.cust_served(50)
obj1.current_customer
obj1.incriment(50)
obj1.current_customer
obj1.incriment(50)
obj1.current_customer
obj1.incriment(50)
obj1.current_customer