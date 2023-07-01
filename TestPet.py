from Pet_Class import Pet

# Create a pet
pet = Pet()

# Ask user for name of the pet
name = input("What is the name of your pet?")
pet.set_name()

# Ask user for the animal type
animal_type = input("What kind of animal is your pet?")
pet.set_animal_type()

# Ask user for the age of the pet
age = input("How old is your pet")
pet.set_age()

print("\n Pet information:")
print("Name:", pet.get_name())
print("Animal Type:", pet.get_animal_type())
print("Age:", pet.get_age())