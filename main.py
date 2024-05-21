import random
import string
    
def generate():
    
    password_length = input("How many characters would you like your password to be? ")

    
    try:
        password_length = int(password_length)
        if password_length < 8 or password_length > 128:
            print("Character length must be between 8 and 128!")
            return
    except ValueError:
        print("Invalid input. Please enter a number between 8 and 128.")
        return

    lower_question = input("Would you like lowercase letters? (y/n): ").lower()
    upper_question = input("Would you like uppercase letters? (y/n): ").lower()
    digit_question = input("Would you like digits? (y/n): ").lower()
    symbol_question = input("Would you like symbols? (y/n): ").lower()

    characters = ""
    if lower_question == 'y':
        characters += string.ascii_lowercase
    if upper_question == 'y':
        characters += string.ascii_uppercase
    if digit_question == 'y':
        characters += string.digits
    if symbol_question == 'y':
        characters += string.punctuation

    
    if not characters:
        print("You must select at least one character set!")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"Generated password: {password}")

generate()
    

 



 