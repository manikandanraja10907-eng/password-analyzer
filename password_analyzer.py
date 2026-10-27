
import string

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add a number")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add a special character")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)

    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Your password meets all the basic checks!")

password = input("Enter a password to analyze: ")
check_password(password)
```
