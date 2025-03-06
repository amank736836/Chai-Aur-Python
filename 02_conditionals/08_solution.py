password = input("Enter your password to check its strength: ")

# password_length = len(password)

if len(password) < 6:
    Strength = "weak"
elif len(password) <= 10:
    Strength = "medium"
elif password.isalnum():
    Strength = "strong"
else:
    Strength = "very strong"

print(f"The strength of your password is {Strength}")
