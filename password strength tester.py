import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Weak: Password should contain both uppercase and lowercase letters."

    # Check for numbers
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."

    # Check for special characters
    special_characters = re.compile('[!@#$%^&*(),.?":{}|<>]')
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets the criteria for strength."

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)
