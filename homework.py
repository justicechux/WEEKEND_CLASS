file = open('fruits.txt', 'a')

while True:
    print("Enter 1 to add fruits: ")
    print("Enter 2 to display all fruits: ")
    print("Enter 3 to empty the list: ")
    print("Enter anything else to break: ")
    choice = int(input("Enter your choice: "))

    if choice == 1: 
        file = open('fruits.txt', 'a')
        fruit_name = input("Enter fruit name: ")
        fruit_name += '\n'
        file.write(fruit_name)
        file.close()
    elif choice == 2:
        file = open('fruits.txt', 'r')
        fruit_list = []
        lines = file.readlines()
        for fruits in lines:
            fruits = fruits.rstrip()
            fruit_list.append(fruits)
        print(fruit_list)
        file.close()

    else:
        break




