num = input("Enter a table number: ")

if num.isdigit():
    num = int(num)
else:
    print("Invalid input")
    exit()


for i in range(1, 11):
    if i == 5:
        continue
    print(num, "x", i, "=", num * i)
