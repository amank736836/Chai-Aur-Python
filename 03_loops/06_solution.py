number = input("Enter a number for factorial: ")

if number.isdigit():
    number = int(number)
else:
    print("Invalid input")
    exit()

factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial of the number is:", factorial)
