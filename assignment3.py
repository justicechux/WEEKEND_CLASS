# a. Write a program to perform the following:
# i.  receive the full name, age and location from a user.
# ii. print out a description message to the user using f strings. The mesage should look like this:
#     Hello <full name>
#     I see you are <age> years old and you reside in <location>
#     NOTE: the full name should be in lower case (use string method)


# b. Write a program that will take request for a user's name and then print the following:
#  i. the complete name
# ii. the length of the name
# iii. the last character of the name


fullname = input("what is your name:  ")
age = input("what is your age: ")
location = input("where are you located: ") 

output = (f"Hello {fullname.lower}, i see you are {age} years old and you reside in {location}")
print(output) 


# user_name = input("what is your name: ")
# length = len(user_name)
# print(length)
# last_character = user_name[-1]   
# print(last_character)
