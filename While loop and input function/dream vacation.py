responces = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    responce= input("if you could visit one place in wolrd, where would you go? ")

    responces[name] = responce

    for name,responce in responces.items():
        print(f"{name} would like to go {responce}") 