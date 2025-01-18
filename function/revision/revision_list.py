cars = ['audi','bmw','subaru']
for car in cars:
    if car == "bmw":
        print(f"{car.upper()}")
    else:
        print(f"{car.title()}")


cars = ['audi','bmw','subaru','mustang']
my_cars = []

for car in cars:
    adding_cars = cars.pop()
    my_cars.append(adding_cars)
print(my_cars)

my_cars = ['audi','bmw','subaru','mustang']
if my_cars:
    for cars in my_cars:
     print(f"adding  {cars}")
else:
    print(f"No cars in garage")
print(f"{my_cars}")


new_cars_launched = ['audi','bmw','subaru','mustang',"defender","range rover"]
available_cars = ['audi','bmw','subaru','mustang',"defender","range rover"]

for cars in new_cars_launched:
    if cars in available_cars:
        print(f"{cars.title()} is available in garage")
    else:
        print(f"{cars.title()} is not available in garage")