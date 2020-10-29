import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

length = input("Enter the length of the password: ")
if(not length.isnumeric()):
    print("Please enter the valid length of the password")
else:
    password = []
    password.extend(s1)
    password.extend(s2)
    password.extend(s3)
    password.extend(s4)
    password=random.sample(password,int(length))
    newPassword = "".join(password)
    print(newPassword)

