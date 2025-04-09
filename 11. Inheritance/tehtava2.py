import random
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
    def drive(self, hours_driven):
        self.travelled_dis += hours_driven * self.current_speed
class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        self.battery_capacity = battery_capacity
class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_volume):
        super().__init__(reg_number, max_speed)
        self.tank_volume = tank_volume
#
def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)  # reg_number, max_speed, battery_capacity
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)  # reg_number, max_speed, tank_volume
#
    electric_car.accelerate(random.randint(0, electric_car.max_speed))
    electric_car.drive(3)
    gasoline_car.accelerate(random.randint(0, gasoline_car.max_speed))
    gasoline_car.drive(3)
#
    print(f"Electric Car {electric_car.reg_number} traveled {electric_car.travelled_dis} km.")
    print(f"Gasoline Car {gasoline_car.reg_number} traveled {gasoline_car.travelled_dis} km.")
if __name__ == "__main__":
    main()
