class restaurant:
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0
    def describe(self):
        long_name = f"{self.name} {self.cuisine}"
        return long_name
    
class Icecreamstand(restaurant):
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)
        self.flavour = f"Vanila", "Strawberry", "Mango" 

    def flavours(self):
        print(f"Available flavours are {self.flavour} in {self.name}")

Ice_and_Melt = Icecreamstand("Ice and Melt", "Ice Cream Parlour")
print(Ice_and_Melt.describe())
Ice_and_Melt.flavours()
Ice_and_Melt.flavour = f"Vanila", "Strawberry", "Mango","Chocolate" 
Ice_and_Melt.flavours()
Ice_and_Melt.flavour = f"Vanila", "Strawberry", "Mango","Chocolate","Pineapple" 
Ice_and_Melt.flavours()