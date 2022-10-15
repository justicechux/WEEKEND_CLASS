import random
import string

length = int(input("Enther the length of password: "))

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits

total = lowercase + uppercase + numbers

temp = random.sample(total,length)

password = "".join(temp)
print(password) 