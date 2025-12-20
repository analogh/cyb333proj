#! /usr/bin/env python3
# Shebang line to specify Python 3 interpreter

# Modules imported for various functionalities
import secrets  # Used for generating cryptographically strong random patterns
import string   # Provides access to various character types (letters, digits, punctuation)
import re       # Regular Expression module

# Password analysis function
def analyze_password(pwd):
    """
    Evaluates a password string based on length, case, and special characters.
    Returns an integer score (0-3).
    """
    score = 0
    feedback = []

    # Criteria 1: Checks length (Minimum 12 characters)
    if len(pwd) >= 12: 
        score += 1
    else: 
        feedback.append("Too short (12+ character recommended).")

    # Criteria 2: Checks complexity using Regular Expressions
    if re.search(r"\d", pwd) and re.search(r"[A-Z]", pwd) and re.search(r"[a-z]", pwd):
        score += 1
    else:
        feedback.append("Missing uppercase, lowercase, and numberic characters.")

    # Criteria 3: Checks for special character(s).
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1
    else:
        feedback.append("Missing special characters.")

    return score, feedback

# Password generation function
def generate_strong_password(length=16):
    """
    Generates a random password using the secrets module.
    Runs a recursive check to ensure the generated password meets 'High' strength criteria.
    """
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    
    while True:
        # Generates a password string of 16 characters for cryptographic resilience
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        
        # Verifies the generated password passes the earlier 'score 3' requirement
        if analyze_password(password)[0] == 3:
            return password

# Main application loop
def main():
    """
    Primary application loop. Evaluates user input and displays results.
    """
    while True:
        print("\n" + "="*30)
        print("--- SecurePass Analyzer ---")
        print("="*30)
        user_input = input("Enter password to analyze (or 'q' to quit): ")
        
        # Exit program condition
        if user_input.lower() == 'q': 
            break
        
        if not user_input: 
            continue

        try:
            score, issues = analyze_password(user_input)
            
            # Text-based markers to indicate status levels (Low, Medium, High)
            if score == 3:
                print("\n[+++ HIGH STRENGTH +++]")
                print("Status: Your password is secure.")
            elif score == 2:
                print("\n[*** MEDIUM STRENGTH ***]")
                print(f"Improvements needed: {', '.join(issues)}")
            else:
                print("\n[!!! LOW STRENGTH !!!]")
                print(f"Danger! Issues found: {', '.join(issues)}")

            # Prompt for password generation if strength is not high
            if score < 3:
                choice = input("\nWould you like to generate a high-strength password? (y/n): ").lower()
                if choice in ['y', 'yes']:
                    new_pwd = generate_strong_password()
                    print("-" * 30)
                    print(f"New Secure Password: {new_pwd}")
                    print("Strength Assessment: HIGH")
                    print("-" * 30)
                    
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Program initiation
if __name__ == "__main__":
    main()