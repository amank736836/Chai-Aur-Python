str = input("Enter a string to reverse: ")
reversed_str = ""

for char in str:
    reversed_str = char + reversed_str 

print("Reversed string:", reversed_str)