def multiple(p1, p2):
    return p1 * p2


v1 = input("Enter a number or text: ")
v2 = input("Enter another number or text: ")

if not v1.isdigit() and not v2.isdigit():
    v1 = int(v1)
    v2 = int(v2)
elif v1.isdigit():
    v1 = int(v1)
elif v2.isdigit():
    v2 = int(v2)
else:
    print("Invalid input. Please enter one number at least.")
    exit()

print(f"The product of {v1} and {v2} is {multiple(v1, v2)}")
