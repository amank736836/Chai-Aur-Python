while True:
    number = input("Enter a number between 1 and 10: ")
    if number.isdigit():
        number = int(number)
    else:
        print("Invalid input")
        exit()

    if number < 1 or number > 10:
        print("Invalid input")
    else:
        print("Valid input")
