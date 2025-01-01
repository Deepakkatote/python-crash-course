sandwitch_order = ["Pastrami","Chesese Sandwitch","Pastrami","Tuna Sandwitch","Pastrami","Veg Masala Sandwitch"]

while "Pastrami" in sandwitch_order:
    sandwitch_order.remove("Pastrami")

finished_sandwitch = []

while sandwitch_order:
    order = sandwitch_order.pop()
    print(f"I made your {order.title()} sandwich")

    finished_sandwitch.append(order)

for fin_sandwitch in finished_sandwitch:
    print(f"your {fin_sandwitch} is ready")

print("Deli is out of Pastrami sandwitch")

