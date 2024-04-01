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
    