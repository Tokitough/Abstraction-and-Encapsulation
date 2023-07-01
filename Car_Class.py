# Car class
class Car:
    
    # Methods
    def __init__ (self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # Add 5 to the speed
    def accelerate (self):
        self.__speed + 5
        return ("The car is going", self.__speed, "km/h")
    
    # Subtract 5 to the speed
    def brake (self):
        self.__speed - 5
        return self.__speed
    
    # Get current speed
    def get_speed(self):
        return self.__speed
    
    # Create a car object
    def create_car (self):
        Zoomy = Car(2004, "Toyota", 0)
        
        i = 1
        while i < 6:
            Zoomy.accelerate()
            i += 1