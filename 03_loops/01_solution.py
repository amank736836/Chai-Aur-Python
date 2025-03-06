numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

positive_numbers_count = 0
positive_numbers_sum = 0
positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers_count += 1
        positive_numbers_sum += number
        positive_numbers.append(number)
print(
    "Final count of positive numbers is:",
    positive_numbers_count,
    "and their sum is:",
    positive_numbers_sum,
    "and the numbers are:",
    positive_numbers,
)
