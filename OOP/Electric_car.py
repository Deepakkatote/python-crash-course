class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name
    
class Battery:
    def __init__(self, battery = 40):
      self.battery = battery
    
    def Battery_description(self):
       print(f"This car is having {self.battery}-kwh capacity")
    
    def range(self):
        if self.battery == 40:
           range = 150
        elif self.battery == 65:
           range = 225
        print(f"This car can go {range} miles in full charge")

    def upgrade_Battery(self):
        if self.battery == 40:
            self.battery = 65
            print(f"Upgrading the Battery to 65-kwh")
        else:
            Print("Battery is already upgraded")


class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


leaf = Electric_car("nissan","leaf", 2024)
print(leaf.describe())
leaf.battery.Battery_description()
leaf.battery.range()
leaf.battery.upgrade_Battery()
leaf.battery.range()