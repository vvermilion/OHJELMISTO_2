
class elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
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
        print(f"The elevator is now on floor {self.current_floor}.")
hissi = elevator(100, 1)
hissi.go_to_floor(10)
hissi.go_to_floor(0)