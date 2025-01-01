from transfer import make_car as mc # type: ignore
from transfer import pijja as pj # type: ignore

pj(41,"Double Cheese", "Margarita", "Paneer Masala")

pj(42,"Farm House","PeriPeri","Veg Masala")

make_car = mc("Force", "Gurkha",colour = 'black', Type = "suv")
print(make_car)

obj2 = mc("TATA", "Range Rover", colour = "black", SUV =True)
print(obj2)
