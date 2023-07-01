from Car_Class import Car

# Create a car object
Zoomy = Car(2004, "Toyota", 0)


# Call accelerate 5 times
print("\u001B[36m=" * 30)
print("\u001B[36m-" * 6 + "\u001B[32mAccelerating Zoomy" + "\u001B[36m-" * 6)
print("\u001B[36m=" * 30)
for i in range(5):
    Zoomy.accelerate()
    print("\u001B[37mZoomy is going", Zoomy.get_speed(), "km/h")
    
# Call brake 5 times   
print("\u001B[36m=" * 30)
print("\u001B[36m-" * 11 + "\u001B[31mBraking" + "\u001B[36m-" * 12)
print("\u001B[36m=" * 30)
for i in range(5):
    Zoomy.brake()
    print("\u001B[37mZoomy is going", Zoomy.get_speed(), "km/h")
    