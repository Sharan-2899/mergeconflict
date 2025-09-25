tickets=1

ticket_cost=150

if tickets == 5:
    print("tickets available...your'e ready to book your tickets")

    if tickets != 0:
            print("*********************")
            print("\nChoose an option: ")
            print("1. Book Ticket")
            print("2. Cancel Ticket")
            print("3. Check Availability")
            print("4. Exit")
            print("")
            print("*********************")

            option=int(input("Enter a option: "))
            print(" ")
            print("*********************")

            if option == 1:
                 print("How many tickets you want to book")
                 if tickets > 0:
                      print(tickets,"are available")
                 else:
                      print("0 tickets are available")     
            elif option == 2:
                 print("How many tickets you want to cancel")    
            elif option == 3:
                 print("wait for available tickets") 
            elif option == 4:
                 print("You chose to exit..have a nice day")          
            else: 
                 print("invalid option")  
             

    else:
        print("Invalid option")        


else:
    print("tickets not available")    