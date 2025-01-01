def sandwich(*item):
    print(f"{item}")

sandwich("cheese")

sandwich("double chesse","veg","panne masala")
sandwich("farmhouse","chille","aalo masala","baigan masala","butter masala")



def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

info = build_profile("Dhruvi", "Krushna", Location = "Shegaon", field = "Python epert")
print(info)


def make_car(manufacturer, model_name,**car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

make_car = make_car('Force','Gurkha', colour = 'Black', SUV = True)
print(make_car)