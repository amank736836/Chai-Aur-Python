weather = input("Provide the weather: ")

if (
    weather.lower() != "rainy"
    and weather.lower() != "sunny"
    and weather.lower() != "snowy"
):
    print("Please provide a valid weather")
    exit()

if weather.lower() == "sunny":
    print("Go for a walk in the park")
elif weather.lower() == "rainy":
    print("Stay at home and read a book")
elif weather.lower() == "snowy":
    print("Go skiing or Build a snowman")
else:
    print("Please provide a valid weather")

