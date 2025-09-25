tickets = 5  
ticket_cost = 150
booked_tickets = 0

while True:
    print("\n*********************")
    print("Choose an option:")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Availability")
    print("4. Exit")
    print("*********************")

    option = int(input("Enter an option: "))
    print(" ")

    if option == 1:
        if tickets > 0:
            num = int(input("How many tickets do you want to book? "))
            if num <= tickets:
                tickets -= num
                booked_tickets += num  # Track bookings properly
                new_cost = num * ticket_cost
                print(f"{num} ticket(s) booked successfully. Remaining tickets: {tickets}")
                print(f"Total cost is: {new_cost}")
            else:
                print(f"Only {tickets} tickets are available.")
        else:
            print("No tickets available to book.")

    elif option == 2:
        if booked_tickets == 0:
            print("You have no booked tickets to cancel.")
        else:
            num = int(input("How many tickets do you want to cancel? "))
            if num <= booked_tickets:
                tickets += num
                booked_tickets -= num
                print(f"{num} ticket(s) cancelled. Tickets now available: {tickets}")
            else:
                print(f"You can only cancel up to {booked_tickets} ticket(s).")

    elif option == 3:
        print(f"Currently, {tickets} ticket(s) available.")

    elif option == 4:
        print("You chose to exit. Have a nice day!")
        break

    else:
        print("Invalid option. Please choose a valid one.")
