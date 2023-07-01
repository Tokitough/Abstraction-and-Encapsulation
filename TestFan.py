from Fan_Class import Fan

class TestFan:

    def test_fan(self):    
        # Create two fan objects
        fan_1 = Fan(Fan.FAST, 10, "yellow", True )
        fan_2 = Fan(Fan.MEDIUM, 5, "blue", False)

        print("Properties of Fan 1:")
        print("Speed:", fan_1.get_speed())
        print("Radius:", fan_1.get_radius())
        print("Color:", fan_1.get_color())
        print("On:", fan_1.is_on())

        print("\nProperties of Fan 2:")
        print("Speed:", fan_2.get_speed())
        print("Radius:", fan_2.get_radius())
        print("Color:", fan_2.get_color())
        print("On:", fan_2.is_on())
  
# Instance of a class to run the test       
test = TestFan()
test.test_fan()
