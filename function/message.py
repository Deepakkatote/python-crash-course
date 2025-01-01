def display_message():
    print("I am learing function in this chapter")

display_message()

def fav_book(title):
    print(f"One of my favrroite book is {title.title()}")

fav_book("maha shiv puran")
fav_book("sunderkand")
fav_book("shiva triology")
fav_book("alice in wonderland")


'''Positional argument(placement of parameter and argument must match)'''
def make_shirt(shirt_type,sije):
    int = sije
    print(f"The sije of the {shirt_type.title()} is {sije}")

make_shirt("oversijed",42)

'''keyword argument: in this we can call argument and parameter at any place'''

def make_shirt(shirt,sije):
    int = sije
    print(f"The sije of {shirt.title()} is {sije}")

make_shirt(sije = 40, shirt="full sleeves")


''' Default value can be stored in paramenter so no need to mention value in argument'''

def make_shirt(sije="large",message="I love Python"):
    print(f"The sirt {sije} has message {message}")

make_shirt()
make_shirt(sije='medium',)
make_shirt(sije="small",message="I love coding")

def describe_city(city,country="India"):
    print(f"{city.title()} is in {country}")

describe_city("Shegaon",)
describe_city("Ujjain")
describe_city(city="Sydney",country="Austrelia")