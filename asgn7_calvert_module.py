# Car class definition
class Car:
    # Constructor
    def __init__(self):
        # Private variables
        self.__distance = 2  # Default distance
        self.__horn = "beep beep"  # Default horn style
        self.__color = ""  # Default color
        self.__line = "-"  # Default line made of hyphens
    
    # Method to sound the horn
    def soundHorn(self):
        print(self.__horn)
    
    # Method to get the color
    def getColor(self):
        return self.__color
    
    # Method to show the line of hyphens
    def showLine(self, distance):
        # Appends the hyphens based on distance
        self.__line += "-" * distance
        return self.__line

# Model_1 class inherited from Car
class Model_1(Car):
    # Constructor
    def __init__(self):
        # Call parent constructor
        super().__init__()
        self.__color = "blue"  # Set color to blue
    
    # Method to get the color
    def getColor(self):
        return self.__color
    
# Model_2 class inherited from Car
class Model_2(Car):
    # Constructor
    def __init__(self):
        # Call parent constructor
        super().__init__()
        self.__color = "red"  # Set color to red
        self.__horn = "honk honk"  # Set horn style
    
    # Method to get the color
    def getColor(self):
        return self.__color
