class SeatBookingSystem:
    """
    A seat booking system for Apache Airlines' Burak757 jets.
    This class provides functionalities to check seat availability, book a seat,
    free a seat, and display the current booking state.
    """
    
    def __init__(self):
        """
        Initializes the seat layout for the airplane and booking details.
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
        self.booking_details = {}  # Dictionary to store booking reference and traveller details

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


    def book_seat(self, seat, reference, passport_number, first_name, last_name):
        """
        Books a specific seat if it is available, assigns a booking reference, and stores user details.
        
        :param seat: A string indicating the seat (e.g., "1A")
        :param reference: A unique booking reference
        :param passport_number: Passport number of the traveler
        :param first_name: First name of the traveler
        :param last_name: Last name of the traveler
        """
        row, column = seat[:-1], seat[-1]
        if column in self.seat_layout and int(row)-1 < len(self.seat_layout[column]):
            if self.seat_layout[column][int(row)-1] == 'F':
                self.seat_layout[column][int(row)-1] = reference  # Mark seat with reference
                # Store booking details
                self.booking_details[reference] = {
                    'passport_number': passport_number,
                    'first_name': first_name,
                    'last_name': last_name,
                    'seat': seat
                }
                print(f"Seat {seat} has been successfully booked with reference {reference}.")
            else:
                print(f"Seat {seat} cannot be booked because it is not available.")
        else:
            print("Invalid seat number.")
    

    def free_seat(self, seat):
        """
        Frees up a booked seat, removes booking details, and marks the seat as available.
        
        :param seat: A string indicating the seat (e.g., "1A")
        """
        row, column = seat[:-1], seat[-1]
        if column in self.seat_layout and int(row)-1 < len(self.seat_layout[column]):
            booking_ref = self.seat_layout[column][int(row)-1]
            if booking_ref not in ['F', 'X', 'S']:  # Check if the seat is booked with a reference
                self.seat_layout[column][int(row)-1] = 'F'  # Mark the seat as free
                # Remove the booking details associated with this reference
                if booking_ref in self.booking_details:
                    del self.booking_details[booking_ref]
                    print(f"Seat {seat} and its booking details have been successfully freed.")
                else:
                    print("Booking reference not found. Seat marked as free.")
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