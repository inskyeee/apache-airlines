class SeatBookingSystem:
    def __init__(self):
        self.seat_layout = {
            'A': ['F']*80,
            'B': ['F']*80,
            'C': ['F']*80,
            'D': ['F']*76 + ['S']*2 + ['F']*2,
            'E': ['F']*76 + ['S']*2 + ['F']*2,
            'F': ['F']*76 + ['S']*2 + ['F']*2,
        }

    def check_availability(self, seat):
            row, column = seat[:-1], seat[-1]
            if column in self.seat_layout and int(row)-1 < len(self.seat_layout[column]):
                status = self.seat_layout[column][int(row)-1]
                if status == 'F':
                    print(f"Seat {seat} is available.")
                else:
                    print(f"Seat {seat} is not available.")
            else:
                print("Invalid seat number.")
    
    def book_seat(self, seat):
        row, column = seat[:-1], seat[-1]
        if column in self.seat_layout and int(row)-1 < len(self.seat_layout[column]):
            if self.seat_layout[column][int(row)-1] == 'F':
                self.seat_layout[column][int(row)-1] = 'R'
                print(f"Seat {seat} has been successfully booked.")
            else:
                print(f"Seat {seat} cannot be booked because it is not available.")
        else:
            print("Invalid seat number.")

    
    def free_seat(self, seat):
        row, column = seat[:-1], seat[-1]
        if column in self.seat_layout and int(row)-1 < len(self.seat_layout[column]):
            if self.seat_layout[column][int(row)-1] == 'R':
                self.seat_layout[column][int(row)-1] = 'F'
                print(f"Seat {seat} has been successfully freed.")
            else:
                print(f"Seat {seat} is not booked.")
        else:
            print("Invalid seat number.")

    def show_booking_state(self):
        print("Current booking state:")
        for column in sorted(self.seat_layout.keys()):
            for row in range(len(self.seat_layout[column])):
                print(f"{row+1}{column}: {self.seat_layout[column][row]}", end='  ')
            print()