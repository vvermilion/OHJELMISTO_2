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
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self, hours):
        print(f"Race status after {hours} hours:")
        print(f"{'Car Reg':<10}{'Distance':<10}{'Speed':<10}")
        print("-" * 30)
        for car in self.cars:
            print(f"{car.reg_number:<10}{car.travelled_dis:<10}{car.current_speed:<10}")
    def race_finished(self):
        for car in self.cars:
            if car.travelled_dis >= self.distance:
                return True
        return False
#
cars = [Car(f"ABC-{i}") for i in range(1, 11)]
#
race = Race("Grand Demolition Derby", 8000, cars)
#
hours = 0
while not race.race_finished():
    hours += 1
    race.hour_passes()
    if hours % 10 == 0:
        race.print_status(hours)
#
race.print_status(hours)
print(f"Rcae finished after {hours} hours.")