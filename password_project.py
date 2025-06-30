import string
import random 

def generate_password(len = 9):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password_chars = [random.choice(uppercase), random.choice(special_chars)]

    for i in range(len - 2):
        password_chars += random.choice(lowercase + digits)
   
    random.shuffle(password_chars)
    password = ''.join(password_chars)

    print(password)
    
generate_password(int(input()))

