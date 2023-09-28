#imports of the required tools/ assets
import string
import random
#Louis Copeland
#Options (More coming soon..)
length_of_password = 16 #Length of the desired password (UI coming soon..) 

def gen_random_pswrd(length):
    characters = string.digits + string.punctuation + string.ascii_letters #Types of characters that the password can be made from ASCII, punctiation, digits
    password = ''.join(random.choice(characters) for _ in range(length)) #From the list of characters the password is generated
    return password 

generated_password = gen_random_pswrd(length_of_password)
print("Generated Password:", generated_password) #Password is printed
