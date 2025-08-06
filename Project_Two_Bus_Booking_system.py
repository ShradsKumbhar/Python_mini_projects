# Mini Bus Ticket Booking
# 1. it shows all available seats.
# 2. when user books seat,  it will not be accessible by other users
# 3. user can cancel the booking
# 4. it will keep track for booking details
import os

# function which takes row and col from user and makes seat booked also returns booked_seat count and details in form of tuple
# Accepts the current set of booked seats.
# Asks for name, age, seat row and column.
# Checks if the selected seat is already booked.
# If valid and not already booked:
# Adds it to the booked_seat_tuple and newly_booked_seats, Updates the booked_seat count.
# Displays the updated seat layout (x = booked, o = available), Asks if user wants to book another seat.
# Books multiple seats and returns: Updated booking set, Count, Newly booked seats
def book_seat(booked_seat_tuple,booked_seat):
    # booked_seat_tuple= set()
    max_Rows =5
    max_Cols =3
    newly_booked_seats = set()

    name_passenger= input('\nEnter passenger name:')
    age_passenger = int(input('Enter age: '))
    seat_row = int(input("Enter row number:"))
    seat_col = int(input("Enter col number:"))
    seat =(name_passenger,age_passenger,seat_row,seat_col)

    if any(s[2] == seat_row and s[3] == seat_col for s in booked_seat_tuple):
        print("Seat already booked")
    elif 0<= seat_row < max_Rows and 0<= seat_col <max_Cols:
        booked_seat_tuple.add(seat)
        newly_booked_seats.add(seat)
        booked_seat+=1
        print("seat booked successfully!!!")
    else:
        print('Invalid seat number.')

    print('Seat Layout')
    for row in range(max_Rows):
        for col in range(max_Cols):
            if any(s[2]==row and s[3]==col for s in booked_seat_tuple):
                print('x', end=' ')
            else:
                print('o', end=' ')
        print('')

    more =input('Wanna book more seats? (Y/N) ')
    if more.lower() =='y':
        next_booked_seat_tuple, next_booked_seat, next_newly_booked = book_seat(booked_seat_tuple, booked_seat)
        return next_booked_seat_tuple, next_booked_seat, newly_booked_seats.union(next_newly_booked)
    else:
        return booked_seat_tuple,booked_seat, newly_booked_seats

#Stores the newly booked seat details in a text file.
# Opens the file in append mode ('a').
# Writes each newly booked seat as a line in the format:
def upload_pass_details_to_file(booked_seat_tuple, filename):
    with open(filename, 'a') as f:
        for seat in booked_seat_tuple:
            f.write(f'{seat[0]},{seat[1]},{seat[2]},{seat[3]}\n')
    # print("Booking details saved to file.")
    print('Thanks for Booking!!!')

# Loads existing booked seats from file into memory at program start.
# Opens file in read mode,Reads each line and splits it into name, age, row, and column.
# Converts each into a tuple and adds to the booking set, Returns the complete set of booked seats.
def get_details_from_file(filename):
    booked_seat_tuple = set()
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    name = parts[0]
                    age = int(parts[1])
                    row = int(parts[2])
                    col = int(parts[3])
                    booked_seat_tuple.add((name, age, row, col))
    except FileNotFoundError:
        print("No booking file found yet. Starting fresh.")
    return booked_seat_tuple

#show available seats at initial
#Displays a seat layout map to the user, just to hel user what is available for booking
def show_seat_layout(booked_seat_tuple, rows=5, cols=3):
    print("\nSeat Layout(O-Available, x-Booked)")
    for row in range(rows):
        for col in range(cols):
            if any(s[2] == row and s[3] == col for s in booked_seat_tuple):
                print('x', end=' ')
            else:
                print('o', end=' ')
        print('')

#Allows a user to cancel a booked seat
#Asks for name, seat row, and column,Searches for a matching booking in the set.
#if finds then it will remove seat from set, rewrited set and confirms
def cancel_booking(booked_seat_tuple, filename):
    name = input("Enter your name: ")
    row = int(input("Enter row number of booked seat: "))
    col = int(input("Enter column number of booked seat: "))

    found = False
    for seat in booked_seat_tuple:
        if seat[0] == name and seat[2] == row and seat[3] == col:
            booked_seat_tuple.remove(seat)
            found = True
            break

    if found:
        with open(filename, 'w') as f:
            for seat in booked_seat_tuple:
                f.write(f'{seat[0]},{seat[1]},{seat[2]},{seat[3]}\n')
        print("Booking cancelled successfully.")
    else:
        print("Booking not found.")

#Clears all bookings and resets the system.
def reset_all_seats(filename):
    open(filename, 'w').close()  # This clears the file contents
    print("All seats have been reset to available.")





#once seat is booked it should not be accessable by any other user and should make cross and then
#booked_seat is to check if there is any seat available in bus to book
# create text file to store seat number and name,age,contact, destination of user
filename= "BusBooking.txt"
booked_seat_tuple = get_details_from_file(filename)
booked_seat = len(booked_seat_tuple)
# print(f"Booking details saved to file: {os.path.abspath(filename)}")
print("Welcome to XYZ Travels!")

print("1. Book Seat")
print("2. Cancel Booking")
print("3. Reset All Seats")
choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    show_seat_layout(booked_seat_tuple)
    booked_seat_tuple, booked_seat, newly_booked_seats = book_seat(booked_seat_tuple, booked_seat)
    upload_pass_details_to_file(newly_booked_seats, filename)
elif choice == '2':
    cancel_booking(booked_seat_tuple, filename)
elif choice == '3':
    reset_all_seats(filename)
else:
    print("Invalid choice.")

