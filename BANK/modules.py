import string
from random import choice


# Create aleatory password
def create_password():
    characters = string.ascii_letters + string.digits + string.ascii_uppercase
    password = ''
    for i in range(10):
        password += choice(characters)
    return password