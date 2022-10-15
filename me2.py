menu = {
    "morning": "bread and tea",
    "post-morning": "ginger tea",
    "afternoon": "Rice and egg",
    "evening": "Spaghetti"
}

menu.get("morning")
print(menu.get("morning"))

dinner_type = input("what meal do you want to eat: ")
meal = menu[dinner_type]
meal = menu.get(dinner_type)
if meal == None: 
    print(f"we dont have a meal for {dinner_type}")
else:
         print(f"your {dinner_type} meal is {meal} ")