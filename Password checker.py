import re

def check_password_strength(password):
    strength = 0  # counter 
    
    # Check password conditions
    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):  # for lowercase
        strength += 1
    if re.search("[A-Z]", password):  # Fixed: Added correct square brackets
        strength += 1
    if re.search("[0-9]", password):  # for numbers
        strength += 1
    if re.search("[!@#$%^&*():{}]", password): # for special character
        strength += 1

    # Fixed: Indented this entire block so it belongs to the function
    if strength <= 2:
        return "Weak ❌"
    elif strength == 3 or strength == 4:
         return "Medium ⚠️"
    else:
         return "Strong ✅"
     
# Main program
password = input("Enter your password: ")
print("Password strength:", check_password_strength(password))