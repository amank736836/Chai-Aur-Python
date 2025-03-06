age = input("Provide your age: ")
day = input("Provide the day of the week: ")

if age.isnumeric():
    age_in_int = int(age)
else:
    print("Please provide a valid number")
    exit()

if (
    day.lower() != "sunday"
    and day.lower() != "saturday"
    and day.lower() != "friday"
    and day.lower() != "thursday"
    and day.lower() != "wednesday"
    and day.lower() != "tuesday"
    and day.lower() != "monday"
):
    print("Please provide a valid day")
    exit()

price = 12 if age >= 18 else 8

# if age_in_int >= 18:
#     price = 12
# else:
#     price = 8

if day.lower() == "wednesday":
    # price = price - 2
    price -= 2

print(f"The price is {price}")
# print("The price is", price)
