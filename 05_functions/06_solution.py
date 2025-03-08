def add(a, b):
    return a + b


def get_number():
    num = input("Enter a number: ")
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input. Please enter a number.")
        exit()


num1 = get_number()
num2 = get_number()

result = add(num1, num2)


print(f"The sum of {num1} and {num2} is {result}")

cube = lambda x: x**3

print(f"The cube of {num1} is {cube(num1)}")
print(f"The cube of {num2} is {cube(num2)}")

print(f"The sum of the cubes of {num1} and {num2} is {cube(num1) + cube(num2)}")
