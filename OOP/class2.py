class restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0
        pass

    def description(self):
        description = f'{self.name} {self.cuisine}'
        return description
    
    def status(self):
        print(f"{self.name} is now open")

    def customer_served(self,customer):
        self.served = customer
        print(f"{self.name} has served {self.served} customer today")


    def increment(self,customer):
        self.served += customer
        print(f"{self.name} has served {self.served} customer today")

obj = restaurant("Paradise", "Pure Veg")
print(obj.description())
obj.status()
obj.customer_served(10)
obj.increment(40)
obj.increment(40)
obj.customer_served(20)
obj.increment(40)