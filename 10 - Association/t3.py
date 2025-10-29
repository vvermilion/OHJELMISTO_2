class elevator:
    def __init__(self, top_floor, bottom_floor, elevator_number):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
        self.elevator_number = elevator_number
#
    def floor_up(self):
        self.current_floor += 1
#
    def floor_down(self):
        self.current_floor -= 1
#
    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if target_floor > self.current_floor:
                self.floor_up()
            elif target_floor < self.current_floor:
                self.floor_down()
        print(f"Elevator {self.elevator_number} is now on floor {self.current_floor}.")
#
class building:
    def __init__(self, top_floor, bottom_floor, elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevators = [elevator(top_floor, bottom_floor, _ + 1)
        for _ in range(elevators)]
    def run_elevator(self, elevator_number, target_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(target_floor)
    def fire_alarm(self):
        print("The fire alarm has been triggered!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
#
rakennus = building(100, 1, 3)
rakennus.run_elevator(1, 10)
rakennus.run_elevator(2,50)
rakennus.run_elevator(3,2)
rakennus.fire_alarm()