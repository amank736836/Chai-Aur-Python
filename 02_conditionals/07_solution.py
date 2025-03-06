order_size = input("Provide the size of the order: Large, Medium, Small: ")

extra_shot = input("Do you want an extra shot? Yes or No: ")

if (
    order_size.lower() != "large"
    and order_size.lower() != "medium"
    and order_size.lower() != "small"
):
    print("Please provide a valid size")
    exit()

if extra_shot.lower() != "yes" and extra_shot.lower() != "no":
    print("Please provide a valid answer")
    exit()

if extra_shot.lower() == "yes":
    coffee = order_size + " Cup of coffee with an extra shot"
else:
    coffee = order_size + " Cup of coffee"

print(f"Your order is: {coffee}")
