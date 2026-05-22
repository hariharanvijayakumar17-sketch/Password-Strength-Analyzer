import re

common_passwords = ["password","123456","qwerty","admin"]

password = input("Enter Password: ")
score = 0

if len(password) >= 8:
    score += 2
if re.search("[A-Z]", password):
    score += 2
if re.search("[a-z]", password):
    score += 2
if re.search("[0-9]", password):
    score += 2
if re.search("[!@#$%^&*]", password):
    score += 2

if password in common_passwords:
    score -= 2

print("Score:", score, "/10")

if score <= 4:
    print("Weak Password")
elif score <= 7:
    print("Medium Password")
else:
    print("Strong Password")

print("Suggested Password:", password + "@2026")
