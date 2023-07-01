# Pet class
class Pet:
    
    # Pet Attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    # Setter 
    # Set the name of the pet
    def set_name (self, name):
        self.__name(input("What is the name of your pet?"))
        return self.__name
    
    # Set the type of animal
    def set_animal_type (self, animal_type):
        self.__animal_type(input("What kind of animal is your pet?"))
        return self.__animal_type
    
    # Set the age of the pet
    def set_age (self, age):
        self.__age(input("How old is your pet?"))
        return self.__age
    
    # Getter
    #Get the name of the pet
    def get_name (self):
        return self.__name
    
    # Get the animal type of the pet
    def get_animal_type (self):
        return self.__animal_type
    
    # Get the age of the pet
    def get_age (self):
        return self.__age