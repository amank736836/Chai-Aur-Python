def add(num1, num2):
    return num1 + num2

one = input("Enter a number: ")

if one.isdigit():
    num1 = int(one)
else :
    print("Invalid input. Please enter a number.")
    exit()

two = input("Enter another number: ")

if two.isdigit():
    num2 = int(two)
else :
    print("Invalid input. Please enter a number.")
    exit()

result = add(num1, num2)

print(f"The sum of {num1} and {num2} is {result}")
