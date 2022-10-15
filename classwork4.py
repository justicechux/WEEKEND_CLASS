# from codecs import getencoder


# write a program to ask the user his/her full name,
# occupation and gender

# hello <fullname>,
# i see you are a <occupation>
# your gender is <gender> n


fullname = input("what is your fullname: ")
occupation = input("enter occupation: ")
gender = input("enter your gender: ")

output = (f"hello {fullname}, i see you are a {occupation}, your gender is {gender}")
print(output)