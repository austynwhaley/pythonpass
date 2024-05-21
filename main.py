import math

lower_case = ['abcdefghijklmnopqrstuvwxyz']
upper_case = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
numbers = ['1234567890']
symbols = ["!#$%&()*+-/:;<=>?@[\]^{|}~"]

def is_nan(value):
    try:
        return math.isnan(float(value))
    except ValueError:
        return True
    
def generate():
    passOption
    passwordLength = input("How many characters would you like your password to be?")
    print((passwordLength))
    if (int(passwordLength) < 8 or int(passwordLength) > 128 or is_nan(passwordLength)):
        print("Characters length must be between 8 and 128!")
        return  
    
generate()
    

 



 