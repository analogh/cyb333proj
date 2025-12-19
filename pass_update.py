#! /usr/bin/env python3

import secrets
import string

def check_strength(password):
    # Checks length and if it contains numbers/letters
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    
    if len(password) >= 12 and has_digit and has_upper:
        return "HIGH"
    elif len(password) >= 8:
        return "MEDIUM"
    else:
        return "LOW"

def suggest_password():
    # Simple password generator
    chars = string.ascii_letters + string.digits + "!"
    return ''.join(secrets.choice(chars) for i in range(12))

# Testing loop
print("--- Password Checker (In-Progress Build) ---")
test_pwd = input("Enter password to test: ")
strength = check_strength(test_pwd)

print("Assessment:", strength)

if strength != "HIGH":
    choice = input("Would you like a suggestion? (y/n): ")
    if choice == 'y':
        print("Suggested:", suggest_password())
