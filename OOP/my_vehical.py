from car import Car # type: ignore
from electric_vehical import ElectricCar as EC  # type: ignore

my_gurkha = Car("force", "gurkha", 2024)
print(my_gurkha.description())
my_gurkha.read_odometer()
my_gurkha.update_odometer(5000)
my_gurkha.read_odometer()
my_gurkha.incremnt_odometer(500)


my_leaf = EC("nissan","leaf", 2024)
print(my_leaf.description())
my_leaf.battery.get_range()
my_leaf.battery.upgrde_battery()
my_leaf.battery.get_range()