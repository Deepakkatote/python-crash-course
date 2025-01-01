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
