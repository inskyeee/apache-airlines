import random
import string
from seats import SeatBookingSystem


# Global set to keep track of all issued booking references
issued_references = set()

def generate_unique_booking_reference():
    """
    Generates a unique booking reference consisting of exactly eight alphanumeric characters.
    Ensures the generated reference is unique by checking against previously issued references.
    
    :return: A unique booking reference string
    """
    while True:
        # Generate a random string of 8 alphanumeric characters
        reference = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        # Check if the generated reference is unique
        if reference not in issued_references:
            issued_references.add(reference)
            return reference



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