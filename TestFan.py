from Fan_Class import Fan

class TestFan:

    def test_fan(self):    
        # Create two fan objects
        fan_1 = Fan(Fan.FAST, 10, "Yellow", True )
        fan_2 = Fan(Fan.MEDIUM, 5, "Blue", False)

        print("\n" + "\u001B[36m-" * 7 + "\u001B[35mProperties of Fan 1" + "\u001B[36m-" * 7)
        print("\u001B[37mSpeed:", fan_1.get_speed())
        print("Radius:", fan_1.get_radius())
        print("Color:\u001B[33m", fan_1.get_color())
        print("\u001B[37mOn:", fan_1.is_on())

        print("\n" + "\u001B[36m-" * 7 + "\u001B[35mProperties of Fan 2" + "\u001B[36m-" * 7)
        print("\u001B[37mSpeed:", fan_2.get_speed())
        print("Radius:", fan_2.get_radius())
        print("Color:\u001B[34m", fan_2.get_color())
        print("\u001B[37mOn:", fan_2.is_on())
  
# Instance of a class to run the test       
test = TestFan()
test.test_fan()
