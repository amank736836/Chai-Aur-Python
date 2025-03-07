number = input("Enter a number to check if it is prime: ")

is_prime = True

if number.isdigit():
    number = int(number)
else:
    print("Invalid input")
    exit()

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
