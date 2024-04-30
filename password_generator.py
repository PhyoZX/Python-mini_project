import random
import string

def generate_password(min_length, numbers = True, special_characters = True) :
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers :
        characters += digits
    if special_characters :
        characters += special
    
    pw = ""
    pw_done = False
    has_number = False
    has_special = False

    while not pw_done or len(pw) < min_length :
        new_char = random.choice(characters)
        pw += new_char

        if new_char in digits :
            has_number = True
        elif new_char in special :
            has_special = True
        
        pw_done = True
        if numbers :
            pw_done = has_number
        if special_characters :
            pw_done = pw_done and has_special
    return pw
 
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

pw = generate_password(min_length, has_number, has_special)
print("Generated password: ", pw)