username = "yetunde2022"
password = "12345678"

input_uesername = input("Enter username")
input_password = input("Enter password")

if input_uesername == username and input_password == password:
    print(f"hello {input_uesername}, login successful")
if input_uesername == username and input_password != password:
    print("incorrect password")
if input_uesername != username and input_password == password:
    print("incorrect uername")
else:  
    print("invalid username or password")