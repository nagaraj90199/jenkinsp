import string

common_passwords = [
    "123456", "password", "admin", "qwerty",
    "abc123", "password123", "letmein"
]

def password_strength(username, password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 1

    # Uppercase check
    if any(c.isupper() for c in password):
        score += 2
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if any(c.islower() for c in password):
        score += 2
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if any(c.isdigit() for c in password):
        score += 2
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if any(c in string.punctuation for c in password):
        score += 2
    else:
        feedback.append("Add at least one special character.")

    # Common password check
    if password.lower() in common_passwords:
        score = 0
        feedback = ["Password is too common and unsafe."]

    # Strength classification
    if score <= 4:
        strength = "WEAK"
    elif score <= 8:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    # Result output
    result = (
        f"User Name: {username}\n"
        f"Password Score: {score} / 11\n"
        f"Strength: {strength}\n"
    )

    if feedback:
        result += "Suggestions:\n"
        for f in feedback:
            result += f"- {f}\n"
    else:
        result += "Password is secure.\n"

    return result


if __name__ == "__main__":
    print(password_strength("Pratham", "Strong@123"))


