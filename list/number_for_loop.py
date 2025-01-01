for number in range(0,21):
 print(number)

num = list(range(1,1000000))
print(min(num))
print(max(num))
print(sum(num))

odd = list(range(1,20,2))
print(odd)

for odds in range(1,20,2):
  print(odds)

multiple_three = list(range(3,33,3))
print(multiple_three)

cubes = []
for value in range(1,11):
  cube = value**3
  cubes.append(cube)
print(cubes)

#Below is the example of list comphrension+
cubes = [value**3 for value in range(1,11)]
print(cubes)

slice = list(range(1,11))
print(f"The first Three numbers from list are {slice[:3]}")
print(f"The first middle numbers from list are {slice[3:6]}")
print(f"The first end numbers from list are {slice[6:]}")

my_pizza = ["margarita","double cheese","farmhouse"]
my_friend_pizza = my_pizza[:]
my_pizza.append("paneer pizza")
print(my_pizza)
my_friend_pizza.append("onian_garlic")
print(my_friend_pizza)

for myfood in my_pizza:
  print(myfood)

for friendfood in my_friend_pizza:
  print(friendfood)

squares = []
for value in range(1,20):
  square = value**2
  squares.append(square)
print(squares)