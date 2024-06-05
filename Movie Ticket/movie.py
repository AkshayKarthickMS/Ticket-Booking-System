import datetime

def read_seats_from_file(file_name):
    seats = []
    with open(file_name, 'r') as file:
        rows, columns = map(int, file.readline().strip().split())
        for line in file:
            row_info = line.strip().split(': ')
            seats_data = row_info[1].split(' ')
            seats.append(seats_data)
    return seats, rows, columns

def write_seats_to_file(file_name, seats):
    with open(file_name, 'w') as file:
        rows = len(seats)
        columns = len(seats[0])
        file.write(f"{rows} {columns}\n")
        for idx, row in enumerate(seats, start=1):
            file.write(f"Row {idx}: {' '.join(row)}\n")

def read_users_from_file(file_name):
    users = {}
    with open(file_name, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            users[username] = password
    return users

def write_users_to_file(file_name, users):
    with open(file_name, 'w') as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")

def read_bookings_from_file(file_name):
    bookings = []
    with open(file_name, 'r') as file:
        for line in file:
            booking_data = line.strip().split(',')
            bookings.append(booking_data)
    return bookings

def write_bookings_to_file(file_name, bookings):
    with open(file_name, 'w') as file:
        for booking in bookings:
            file.write(','.join(booking) + '\n')

def register_user(users_file):
    print("Registration:")
    username = input("Enter your username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return

    password = input("Enter your password: ")
    users[username] = password
    write_users_to_file(users_file, users)
    print("Registration successful!")

def login_user(users_file):
    print("Login:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def display_seats(seats):
    print("Available Seats:")
    for idx, row in enumerate(seats, start=1):
        print(f"Row {idx}: {' '.join(row)}")

def book_tickets(seats, num_tickets):
    booked_seats = []
    for _ in range(num_tickets):
        while True:
            try:
                row_num = int(input("Enter the row number: ")) - 1
                seat_num = int(input("Enter the seat number: ")) - 1

                if 0 <= row_num < len(seats) and 0 <= seat_num < len(seats[0]):
                    if seats[row_num][seat_num] == 'O':
                        seats[row_num][seat_num] = 'X'
                        booked_seats.append((row_num, seat_num))
                        break
                    else:
                        print("Seat already booked. Please select another seat.")
                else:
                    print("Invalid row or seat number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter valid row and seat numbers.")
    return booked_seats

def generate_invoice(booking_id, booked_seats, user_details):
    total_price = 190 * len(booked_seats)
    invoice = f"Invoice\nBooking ID: {booking_id}\nUser Details: {user_details}\nBooked Seats: {', '.join([f'Row {row+1}, Seat {seat+1}' for row, seat in booked_seats])}\nTotal Amount: Rs.{total_price}"
    print(invoice)
    return total_price

def main():
    users_file = "users.txt"
    seats_file = "seats.txt"
    bookings_file = "bookings.txt"

    global users
    users = read_users_from_file(users_file)

    while True:
        print("\nWelcome to Movie Ticket Booking System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            register_user(users_file)
        elif choice == "2":
            if login_user(users_file):
                seats, rows, columns = read_seats_from_file(seats_file)
                bookings = read_bookings_from_file(bookings_file)

                while True:
                    print("\n1. Display Available Seats")
                    print("2. Book Ticket")
                    print("3. Logout")
                    sub_choice = input("Enter your choice (1/2/3): ")

                    if sub_choice == "1":
                        display_seats(seats)
                    elif sub_choice == "2":
                        try:
                            num_tickets = int(input("\nEnter the number of tickets you want to book: "))
                            if num_tickets <= 0:
                                raise ValueError

                            user_first_name = input("Enter your first name: ")
                            user_last_name = input("Enter your last name: ")
                            user_age = int(input("Enter your age: "))
                            user_mobile_number = input("Enter your mobile number: ")
                            user_city = input("Enter your city: ")

                            user_details = f"Name: {user_first_name} {user_last_name}, Age: {user_age}, Mobile: {user_mobile_number}, City: {user_city}"

                            booked_seats = book_tickets(seats, num_tickets)
                            total_amount = generate_invoice(f"BOOKING_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", booked_seats, user_details)

                            write_seats_to_file(seats_file, seats)

                            booking_data = [datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), user_details, f"{', '.join([f'Row {row+1}, Seat {seat+1}' for row, seat in booked_seats])}", str(total_amount)]
                            bookings.append(booking_data)
                            write_bookings_to_file(bookings_file, bookings)

                        except ValueError:
                            print("Invalid input. Please try again.")
                    elif sub_choice == "3":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()