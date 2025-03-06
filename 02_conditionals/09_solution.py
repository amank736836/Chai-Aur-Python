year = input("Provide the year: ")

if year.isnumeric():
    year_in_int = int(year)
else:
    print("Please provide a valid number")
    exit()

if year_in_int % 4 == 0:
    if year_in_int % 100 == 0:
        if year_in_int % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# if year_in_int % 4 == 0 and year_in_int % 100 != 0 or year_in_int % 400 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# if (year_in_int % 400 == 0) or (year_in_int % 4 == 0 and year_in_int % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")
