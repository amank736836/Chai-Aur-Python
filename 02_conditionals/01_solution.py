age = input("Provide your age: ")

if age.isnumeric():
    age_in_int = int(age)
else:
    print("Please provide a valid number")
    exit()

if age_in_int < 13:
    print("Child")
elif age_in_int < 20:
    print("Teenager")
elif age_in_int < 60:
    print("Adult")
else:
    print("Senior")
