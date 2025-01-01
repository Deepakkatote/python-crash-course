class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def description(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,Milegae):
        if Milegae >= self.odometer_reading:
            self.odometer_reading = Milegae
        else:
            print(f"You cannot roll back odometer")

    def incremnt_odometer(self,milegae):
        self.odometer_reading += milegae
        print(f"This car has {self.odometer_reading} miles on it")


class ElectricCar:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()
    
    def description(self):
     long_name = f"{self.make} {self.model} {self.year}"
     return long_name.title()

class Battery:
    def __init__(self,battery = 40):
        self.battery = battery
    
    def Battery(self):
        print(f"This car has {self.battery}-kwh on it")

    def get_range(self):
        if self.battery == 40:
            range = 150
        elif self.battery == 65:
            range = 225
        print(f"This car can go {range} miles on full charge")
    
    def upgrde_battery(self):
        if self.battery == 40:
            self.battery = 65
            print(f"Upgrading Battery to 65 -kwh")
        else:
            print(f"This Battery is already upgraded")

my_gurkha = Car("force", "gurkha", 2024)
print(my_gurkha.description())
my_gurkha.read_odometer()
my_gurkha.update_odometer(5000)
my_gurkha.read_odometer()
my_gurkha.incremnt_odometer(500)


my_leaf = ElectricCar("nissan","leaf", 2024)
print(my_leaf.description())
my_leaf.battery.get_range()
my_leaf.battery.upgrde_battery()
my_leaf.battery.get_range()