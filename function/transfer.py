def pijja(sije, *toppings):
 print(f"makeing {sije} sije of pijja with following toppings")

 for topping in toppings:
    print(f" -{topping}")

def make_car(manufacturer,modal_name,**car_info):
    car_info['Manufacturer'] = manufacturer
    car_info["Model_name"] = modal_name
    return car_info