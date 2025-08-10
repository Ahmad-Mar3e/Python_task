"""
The random module can give me a random number within a certain range.
To use this, I can create a list containing all letters, digits, and symbols,
and let random generate a random number to use as an index.
I will also use the string module to get all letters and digits.
"""
import random as rd
import string

password = ""
uppercase_letters = list(string.ascii_uppercase)  # string module returns a string, so we must turn it into a list
lowercase_letters = list(string.ascii_lowercase)
digits = list(string.digits)
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]

all_characters = uppercase_letters + lowercase_letters + digits + special_characters

# rd.shuffle(all_characters)
# If we want to shuffle the list before picking characters from it, we can use this line I commented it out because I noticed the random password generated without shuffle is better.

number = int(input("Enter the number of characters: "))
for i in range(number):
    password += all_characters[rd.randint(0, len(all_characters) - 1)]  # Fixed: -1 so index is valid
print(password)
