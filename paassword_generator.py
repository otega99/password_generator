import string
import random

characters=[string.ascii_lowercase,
            string.ascii_uppercase,
            [str(i) for i in range(10)]]

def generate_password():
    password=''
    for i in range(10):
        character_group=characters[random.randint(0, 2)]
        password+=character_group[random.randint(0, len(character_group)-1)]
    return password
    
passwords=[generate_password() for i in range(10)]

for password in passwords:
    print(password)
