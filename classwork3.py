my_fruits = ["apple", "mango", "orange", "pineapple"]

print(my_fruits[1])

my_fruits[3] = "coconut"

print(my_fruits[3])


namez = ("ola", "bayo", "lekan", "remi")
namez = list(namez)
namez[2] = "univelcity"
namez = tuple(namez)
print(namez)

person = {
    "name" : "justice",
    "hobbies" : ["dancing", "singing", "gaming"],
    "menu" : {
        "morning" : "fried rice and chicken",
        "afternoon" : "tea",
        "evening" : "semo and egusi"
    }
}

# print(person["menu"]["evening"])
# print(person["hobbies"][1])
person["menu"]["evening"] = "pounded yam"
print(person["menu"]["evening"])




