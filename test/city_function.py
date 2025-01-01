def city_country(city,country,population =''):
    if population:
        long_name = f"{city}, {country} -{population}"
    else:
        long_name = f"{city}, {country}"
    return long_name.title()

tokyo = city_country("tokyo", "Japan",50000)
print(tokyo)