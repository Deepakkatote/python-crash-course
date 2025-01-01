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