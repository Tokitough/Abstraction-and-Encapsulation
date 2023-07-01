from Car_Class import Car

# Create a car object
Zoomy = Car(2004, "Toyota", 0)

# Call accelerate 5 times
print("Accelerating Zoomy")
for i in range(5):
    Zoomy.accelerate()
    print("Zoomy is going", Zoomy.get_speed(), "km/h")

# Call brake 5 times
print("Braking")
for i in range(5):
    Zoomy.brake()
    print("Zoomy is going", Zoomy.get_speed(), "km/h")
    