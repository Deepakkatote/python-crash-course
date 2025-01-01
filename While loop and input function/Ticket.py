prompt = ("Enter your age: ")

while True:
    age = int(input(prompt))
    if age < 3:
        print("The tickrt is free")
    elif age < 13:
        print("The ticket is rupees 10")
    else:
        print("The ticket is rupees 15")2
