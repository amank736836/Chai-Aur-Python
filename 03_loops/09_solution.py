items = [
    "apple",
    "banana",
    "orange",
    "pear",
    "grapes",
    "apple",
    "grapes",
]

unique_items = []

for item in items:
    if item in unique_items:
        print("Duplicate item found:", item)
    else:
        unique_items.append(item)

print("Unique items are:", unique_items)
