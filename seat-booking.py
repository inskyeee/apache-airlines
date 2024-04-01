class SeatBookingSystem:
    """
    A seat booking system for Apache Airlines' Burak757 jets.
    This class provides functionalities to check seat availability, book a seat,
    free a seat, and display the current booking state.
    """
    
    def __init__(self):
        """
        Initializes the seat layout for the airplane.
        - 'F' indicates a free seat
        - 'R' indicates a reserved seat
        - 'X' denotes an aisle
        - 'S' denotes a storage area
        """
        self.seat_layout = {
            'A': ['F']*80,
            'B': ['F']*80,
            'C': ['F']*80,
            'D': ['F']*76 + ['S']*2 + ['F']*2,
            'E': ['F']*76 + ['S']*2 + ['F']*2,
            'F': ['F']*76 + ['S']*2 + ['F']*2,
        }  # Aisles are marked but not stored as they are constant and not bookable

    def check_availability(self, seat):
            """
            Checks if a specific seat is available for booking.
            
            :param seat: A string indicating the seat (e.g., "1A")
            """
            row, column = seat[:-1], seat[-1] # Extract row and column from the seat number
            if column in self.seat_layout and int(row)-1 < len(self.seat_layout[column]): # Check if the seat number is valid   
                status = self.seat_layout[column][int(row)-1] # Get the status of the seat
                if status == 'F':
                    print(f"Seat {seat} is available.")
                else:
                    print(f"Seat {seat} is not available.")
            else:
                print("Invalid seat number.")
    
    def book_seat(self, seat):
        """
        Books a specific seat if it is available.
        
        :param seat: A string indicating the seat (e.g., "1A")
        """
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
        """
        Frees up a booked seat.
        
        :param seat: A string indicating the seat (e.g., "1A")
        """
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
        """
        Displays the current booking state of all seats.
        """
        print("Current booking state:")
        for column in sorted(self.seat_layout.keys()):
            for row in range(len(self.seat_layout[column])):
                print(f"{row+1}{column}: {self.seat_layout[column][row]}", end='  ')
            print()

def main():
    """
    Main function to run the seat booking application.
    It displays a menu and processes user input.
    """
    system = SeatBookingSystem()
    while True:
        print("\n--- Apache Airlines Seat Booking System ---")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        choice = input("Enter your choice: ")
        
        # Process user input based on the choice
        if choice == '1':
            seat = input("Enter seat number (e.g., '1A'): ")
            system.check_availability(seat)
        elif choice == '2':
            seat = input("Enter seat number to book (e.g., '1A'): ")
            system.book_seat(seat)
        elif choice == '3':
            seat = input("Enter seat number to free (e.g., '1A'): ")
            system.free_seat(seat)
        elif choice == '4':
            system.show_booking_state()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()

