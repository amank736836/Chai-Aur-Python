def sum_all(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
    # return sum(args)


print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2))  # 3
