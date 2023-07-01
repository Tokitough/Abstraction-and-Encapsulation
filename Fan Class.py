class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Constructor 
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
        
    