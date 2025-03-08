def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = input("Enter a number for factorial: ")

if number.isdigit():
    number = int(number)
else:
    print("Invalid input")
    exit()

print("Factorial of the number is:", factorial(number))
