dinner_list = ["Dhruvi","Krushna","Didu"]
print(f"{dinner_list[0]} you are invited for dinner")
print(f"{dinner_list[1]} you are invited for dinner")
print(f"{dinner_list[2]} you are invited for dinner\n")
print(f'{dinner_list[0]} cannot make for dinner')
dinner_list[0] = "Deepak"
print(f"\n{dinner_list[0]} you are invited for dinner")
print(f"{dinner_list[1]} you are invited for dinner")
print(f"{dinner_list[2]} you are invited for dinner\n")
print(f"We have invited more guest for dinner\n")
dinner_list.insert(0,"Babu")
dinner_list.insert(2,"Raju")
dinner_list.append("Ravi")
print(dinner_list)
print(f"\n{dinner_list[0]} you are invited for dinner")
print(f"{dinner_list[1]} you are invited for dinner")
print(f"{dinner_list[2]} you are invited for dinner")
print(f"{dinner_list[3]} you are invited for dinner")
print(f"{dinner_list[4]} you are invited for dinner")
print(f"{dinner_list[5]} you are invited for dinner\n")
length = len(dinner_list)
print(f"we have invited {length} guest for dinner")
dinner_list.pop(5)
print("Sorry Ravi we cannot invite you for a dinner")
dinner_list.pop(2)
print("Sorry Raju we cannot invite you for a dinner")
dinner_list.pop(1)
print("Sorry Deepak we cannot invite you for a dinner\n")
print(dinner_list)
del dinner_list[0]
del dinner_list[1]

print(dinner_list)
del dinner_list[0]
print(dinner_list)