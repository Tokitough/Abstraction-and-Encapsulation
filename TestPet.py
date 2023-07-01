from Pet_Class import Pet

# Create a pet
pet = Pet()

print("\u001B[36m=" * 35)
# Ask user for name of the pet
name = input("\u001B[37mWhat is the name of your pet?\n")
pet.set_name(name)

print("\u001B[36m=" * 35)
# Ask user for the animal type
animal_type = input("\u001B[37mWhat kind of animal is your pet?\n")
pet.set_animal_type(animal_type)

print("\u001B[36m=" * 35)
# Ask user for the age of the pet
age = input("\u001B[37mHow old is your pet (in years)?\n")
pet.set_age(age)

# Display Pet Information
print("\n" + "\u001B[36m-" * 7 + "\u001B[34mPet information" + "\u001B[36m-" * 7)
print("\u001B[36m=" * 30)
print("\u001B[37mName:", pet.get_name())
print("Animal Type:", pet.get_animal_type())
print("Age (in years):", pet.get_age())
print("\u001B[36m=" * 30)