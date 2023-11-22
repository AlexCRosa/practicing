import string
import random

# Ask user the amount of characters for the new password
amount_characters = int(input("How many characters the password must have? "))

# Generator logic
def password_generator():
    characters_counter = 0
    password = ""

    # a-z, A-Z, 0-9
    while characters_counter < amount_characters:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        characters_counter += 1

    return password

password = password_generator()

print(password)