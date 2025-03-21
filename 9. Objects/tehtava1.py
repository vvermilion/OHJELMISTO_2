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


