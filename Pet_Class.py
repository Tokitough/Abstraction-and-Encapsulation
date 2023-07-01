# Pet class
class Pet:
    
    # Pet Attributes
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    
    # Setter 
    # Set the name of the pet
    def set_name (self, name):
        self.__name = name
    
    # Set the type of animal
    def set_animal_type (self, animal_type):
        self.__animal_type = animal_type
    
    # Set the age of the pet
    def set_age (self, age):
        self.__age = age
    
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