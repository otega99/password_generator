import string
import random

#this array named characters contains the lowercase letters,
#uppercase letters and the numbers 0 to 9 each as items in the list
characters=[string.ascii_lowercase,
            string.ascii_uppercase,
            [str(i) for i in range(10)]]

def generate_password():
    #the password variable is initialized as an empty string
    password=''
    for i in range(10):
        #here we choose an item in the list characters
        item=characters[random.randint(0, 2)]
        #here we choose a character or digit from the item chosen above 
        password+=item[random.randint(0, len(item)-1)]
    return password
    
passwords=[generate_password() for i in range(10)]

#this for loop will generate ten random passwords 
#using the generate_password() function
for password in passwords:
    print(password)
    
    
