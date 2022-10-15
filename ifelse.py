from unicodedata import name


namwe = input("enter your name: ")
age = int(input("enter your age: "))

if age >= 0 and age <= 4:
    print(f"Hello {name}, you are still a baby")
elif age>= 5 and age <= 12:
    print(f"Hello {name}, you are still a chuld")
elif age >= 13 and age <= 19:
    print(f"Hello {name}, you are a teenager ")
elif age >= 20 and age <= 50:
    print(f"Hello {name}, you are an adult")
elif age >= 51: 
    print(f"Hello {name}, you are an elder")