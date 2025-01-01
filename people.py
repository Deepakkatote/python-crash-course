person_1 = {"first_name": "Dhruvi", "last_name": "Krushna", "age": 7, "city": "Shegaon"}
person_2 = {"first_name": "Deepak", "last_name": "K", "age": 30, "city": "Bawanbir"}

people = [person_1, person_2]
for pep in people:
    print(pep)


animal_1 = {"Animal":"Cat", "Owner":"Dhruvi"}
animal_2 = {"Animal":"Dog", "Owner":"Didu"}
animal_3 = {"Animal":"Cow", "Owner":"Krushna"}
animal_4 = {"Animal":"Liom", "Owner":"Deepak"}

pet = [animal_1,animal_2,animal_3,animal_4]
for pets in pet:
    print(pets)

favroite_places = {"Dhruvi": "Anand Sagar", "Deepak": "Goa", "Krushna": "Water park"}
for favroite_place in favroite_places.items():
   print(favroite_place)


favroite_number = {"Deepak" : [1,2],
                   "Dhruvi": [3,4],
                   "Krushna": [5,6],
                   "Didu": [7,8]
                   }
for name, num in favroite_number.items():
    print(f"{name.title()} favroite numbers are: ")
    for numbers in num:
        print(numbers)
        
cities = {"UjJain": {"Country": "India","Fact": "Mahakaleswar Jotirling"},
          "Varanasi": {"Country": "India","Fact":"Kaal Bhairav"}}

for place, place_info in cities.items():
    print(f"Place: {place}")
    Info = f"{place_info["Fact"]} {place_info["Country"]}"
    print(f"{Info.title()}")
