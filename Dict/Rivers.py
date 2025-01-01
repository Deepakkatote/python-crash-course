rivers = {"Ganaga" : "India",
          "Yamuna": "India",
          "Kaveri": "India",
          "Alaknanda": "India",
          "Saraswati": "India"
          }
for river,country in rivers.items():
    print(f"The {river} runs through {country}")
for river in rivers.keys():
    print(river)
for river in rivers.values():
    print(river)