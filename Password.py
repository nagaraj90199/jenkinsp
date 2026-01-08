import string

common_passwords = [
    "123456", "password", "admin", "qwerty",
    "abc123", "password123", "letmein"
]

def password_strength(username, password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 2
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 2
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 2
    else:
        feedback.append("Add at least one number.")

    if any(c in string.punctuation for c in password):
        score += 2
    else:
        feedback.append("Add at least one special character.")

    if password.lower() in common_passwords:
        score = 0
        feedback = ["Password is too common and unsafe."]

    if score <= 4:
        strength = "WEAK"
    elif score <= 8:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

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
    username = "Nagaraj"
    password = "Strong@123"
    print(password_strength(username, password))
