str = input("Enter a string to check non repeating characters: ")

for char in str:
    if str.count(char) == 1:
        print("First non-repeating character is:", char)
        break
