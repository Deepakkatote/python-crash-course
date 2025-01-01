class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def long_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
        
    def give_raise(self):
        self.salary += 5000
        print(f"The annual salary of {self.first_name} {self.last_name} is {self.salary}")
    
    def custom_raise(self,increment):
        self.salary += increment
        print(f"The annual salary of {self.first_name} {self.last_name} is {self.salary}")
    
dhruvi = Employee("Dhruvi", "Arulkar", 200000)
print(dhruvi.long_name())
dhruvi.custom_raise(10000)

deepak = Employee("Deepak", "Katote", 200000)
print(deepak.long_name())
deepak.give_raise()