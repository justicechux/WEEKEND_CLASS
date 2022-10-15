from secrets import choice


while True:
    print("press 1 to play....and press 2 to end")
    choice = int(input("enter your choice: "))
    if choice == 1:
        fname = input("enter your first name: ")
        lname =  input("enter your last name: ")
        print(f"your full name is {fname} {lname}")
    else:
        break
