'''Exercise 01.02 - Elevator'''
class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        if floor > self.max_floor or floor < 1:
            print("Invalid Floor!")
            return
        self.current_floor = floor

    def report_current_floor(self):
        print(self.current_floor)

def main():
    '''Driver Code'''
    elevator = Elevator(int(input()))
    floor = input()
    while floor != "Done":
        elevator.go_to_floor(int(floor))
        floor = input()
    elevator.report_current_floor()

if __name__ == "__main__":
    main()
