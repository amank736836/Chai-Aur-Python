def even_generator(limit):
    for i in range(0, limit + 1, 2):
        yield i

limit = input("Enter a limit: ")

if limit.isdigit():
    limit = int(limit)
else:
    print("Invalid input. Please enter a number.")
    exit()

for num in even_generator(limit):
    print(num)