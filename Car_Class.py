# Car class
class Car:
    
    # Methods
    def __init__ (self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # Add 5 to the speed
    def accelerate (self):
        self.__speed += 5
        return self.__speed
    
    # Subtract 5 to the speed
    def brake (self):
        if self.__speed >= 5:
            self.__speed -= 5
        else: self.__speed = 0
        return self.__speed
    
    # Get current speed
    def get_speed(self):
        return self.__speed

