# amount = "five thousand"
# name = "david"

# print(f"hello {name},you have {amount} naira as your balance")

# this is a list
# fruits = ["mango", "orange", "pawpaw", "apple"]
# print(fruits[0])
# print(fruits[3])

student = {
        "esther":{
            "fullname": "esther iyi",
            "class": "300 level",
            "cgpa": 4.5,
            "courses_taken": {
                "maths": 50,
                "english": 70,
                "chemistry": 80,
            }
        },
        "ade":{
            "fullname": "ade james",
            "class": "200 level",
            "cgpa": 4.5,
            "courses_taken": {
                "maths": 90,
                "english": 100,
                "chemistry": 40,
            }
        }

    }

print(student["ade"]["courses_taken"]["maths"])
print(student["ade"]["cgpa"])
print(student["esther"]["class"])