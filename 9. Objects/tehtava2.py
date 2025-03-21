class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.travelled_dis = 0
        self.current_speed = 0
    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
#
car1 = Car("ABC-123", 142)
#
print(f"New car: \n"
    f"Registration number {car1.reg_number} \n"
    f"Max speed {car1.max_speed} km/h \n"
    f"Current speed {car1.current_speed} km/h \n"
    f"Travelled distance {car1.travelled_dis} km")
#
print()
#
car1.accelerate(30)
print(f"Current speed: {car1.current_speed} km/h \n")
car1.accelerate(70)
print(f"Current speed: {car1.current_speed} km/h \n")
car1.accelerate(50)
print(f"Current speed: {car1.current_speed} km/h \n")
car1.accelerate(-200)
print(f"Current speed: {car1.current_speed} km/h \n")
