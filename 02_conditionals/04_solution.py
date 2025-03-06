fruit = input("Provide the name of the fruit: ")

if fruit.lower() != "banana":
    print("Please provide a valid fruit")
    exit()

color = input("Provide the color of the fruit: ")

if color.lower() != "yellow" and color.lower() != "green" and color.lower() != "brown":
    print("Please provide a valid color")
    exit()

if color.lower() == "green":
    print("The banana is not ripe yet")
elif color.lower() == "yellow":
    print("The banana is ripe")
else:
    print("The banana is overripe")
