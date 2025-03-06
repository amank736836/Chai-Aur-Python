distance = input("Provide the distance in km: ")

if distance.isnumeric():
    distance_in_int = int(distance)
else:
    print("Please provide a valid number")
    exit()

if distance_in_int < 3:
    transport = "Walk To Your Destination"
elif distance_in_int <= 15:
    transport = "Take a Bike"
elif distance_in_int <= 50:
    transport = "Take a Car"
else:
    transport = "Take a Plane"

print(f"AI recommends you to {transport}")
