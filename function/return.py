'''Define simple function and use return value" to store output in memory"'''

def city_country(city,country):
    print(f"{city.title()}, {country.title()}")
    return

"""When you use "resurn value" VARIABLE is required to call that function value to the body"""
obj1 = city_country('shegaon', 'India')
obj2 = city_country('santiago', 'chile')
obj3 = city_country(country='India', city="ujjain")
print(obj1)
print(obj2)
print(obj3)