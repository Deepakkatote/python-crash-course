fav_language = {
                "Dhruvi": "Python",
                "Deepak": "C",
                "Krushna": "Python",
                "Ravi": "php",
                "Raju": ".net"
                }
for names in fav_language.keys():
    print(f"Hi {names} thank you for taking poll")
if "Didu"  not in fav_language.keys():
 print("didu please take the pool")

friend = ["Ravi","Raju"]
for names in fav_language.keys():
   print(f"Hi {names}")
   if names in friend:
      lanuage = fav_language[names]
      print(f"Hi {names} I see you like {lanuage}")
