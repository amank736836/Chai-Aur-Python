def square_of_num(num):
    # print(num**2)
    return num**2


numInput = input("Enter a number: ")

if numInput.isdigit():
    num = int(numInput)
    result = square_of_num(num)
    print(f"The square of {num} is {result}")
else:
    print("Invalid input. Please enter a number.")
