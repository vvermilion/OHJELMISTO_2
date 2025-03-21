#Write a Car class that has the following properties:
# registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on
# parameter values. The current speed and travelled distance of a new car must
# be automatically set to zero. Write a main program where you create a new car
# (registration number ABC-123, maximum speed 142 km/h). Finally, print out all
# the properties of the new car.
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.travelled_dis = 0
        self.current_speed = 0

car1 = Car("ABC-123", "142 km/h")

print(f"New car: \n"
    f"Registration number {car1.reg_number} \n"
    f"Max speed {car1.max_speed} \n"
    f"Current speed {car1.current_speed} km/h \n"
    f"Travelled distance {car1.travelled_dis} km")


