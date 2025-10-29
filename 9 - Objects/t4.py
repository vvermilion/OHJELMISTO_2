import random
#
class Car:
    def __init__(self, reg_number):
        self.reg_number = reg_number
        self.max_speed = random.randint(100, 200)
        self.travelled_dis = 0
        self.current_speed = 0
#
    def accelerate(self, speed_change):
        self.current_speed += speed_change
#
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
#
    def drive(self, hours_driven):
        self.travelled_dis += hours_driven * self.current_speed
#
cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    car = Car(reg_number)
    cars.append(car)
#
race_finish = False
hours = 0
#
while not race_finish:
    hours += 1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_dis >= 10000:
            race_finish = True
            break
print(f"Race finished after {hours} hours.")
for car in cars:
    print(f"Car {car.reg_number}: {car.travelled_dis} km, "
    f"Max Speed: {car.max_speed} km/h")