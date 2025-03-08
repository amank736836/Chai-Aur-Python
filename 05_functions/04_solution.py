import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radiusInput = input("Enter the radius of the circle: ")

if radiusInput.isdigit():
    radius = int(radiusInput)
else:
    print("Invalid input. Please enter a number.")
    exit()

area, circumference = circle_stats(radius)

print(f"The area of the circle is {round(area,2)} and the circumference is {circumference:.2f}")