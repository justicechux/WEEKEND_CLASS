my_name = "JUSTICE"
year = 2022
print(type(my_name))
print(type(year))
fruits = ["banana",  "mango" ]
fruits = ("apple", "pear", "watermelon")

patients = {
    "esther":{
        "fullname" : "esther iyi", 
        "ailment" : "nil",
        "isfine"  : True, 
        "drugs_taken" : {
            "morning": "panadol",
            "afternoon" : "paracetamol" ,
        "evening" : "just fruits",
        
        }
        
        }
}

print(patients["esther"]["fullname"])
print(patients["esther"]["drugs_taken"]["morning"])
print(patients["esther"]["isfine"])
