score = input("Provide your score: ")

if score.isnumeric():
    if int(score) < 0 or int(score) > 100:
        print("Please provide a valid score")
        exit()

    score_in_int = int(score)
else:
    print("Please provide a valid number")
    exit()

if score_in_int >= 90:
    grade = "A"
elif score_in_int >= 80:
    grade = "B"
elif score_in_int >= 70:
    grade = "C"
elif score_in_int >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")
# print("Your grade is", grade)
