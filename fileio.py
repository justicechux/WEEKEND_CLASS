file = open('fruits.txt', 'a')

while True: 
    print("Enter 1 to add fruits\nEnter anything else to break")
    choice = int(input("Enter your choice: "))
    if choice == 1: 
        fruit_name = input("what is the fruit name: ")
        fruit_name += '\n'
        file.write(fruit_name)

    else:
        break