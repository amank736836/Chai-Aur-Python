pet_species = input("What species is your pet? ")

if pet_species.lower() != "dog" and pet_species.lower() != "cat":
    print("Please provide a valid species")
    exit()

pet_age = input("How old is your pet? ")

if pet_age.isnumeric():
    pet_age_in_int = int(pet_age)
else:
    print("Please provide a valid age")
    exit()

if pet_species.lower() == "dog":
    if pet_age_in_int <= 2:
        print("Puppy Food")
    else:
        print("Adult Dog Food")
else:
    if pet_age_in_int <= 2:
        print("Kitten Food")
    else:
        print("Adult Cat Food")
