valid_card = input("Insert a card: ")
balance = 0

if valid_card.lower() in ['sbi', 'icici', 'hdfc', 'axis']:
    print("----------WELCOME TO ATM------------")

    attempts = 0
    correct_pin = "1234"

    
    while attempts < 3:
        pin = input("Enter your PIN: ")
        if pin == correct_pin:
            print("PIN accepted!\n")

            
            while True:
                print("*********************")
                print("\nChoose an option: ")
                print("1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")
                print("*********************\n")

                option = int(input("Enter your choice: "))
                print("*********************\n")

                if option == 1:
                    print("Your balance is: ₹", balance, "\n")

                elif option == 2:
                    if balance <= 0:
                        print("Zero balance, please deposit first...\n")
                    else:
                        withdraw_amount = int(input("Enter amount to withdraw: "))
                        if withdraw_amount <= balance:
                            balance -= withdraw_amount
                            print(f"You have withdrawn ₹{withdraw_amount}")
                            print("Remaining balance: ₹", balance, "\n")
                        else:
                            print("Insufficient balance\n")

                elif option == 3:
                    deposit_amount = int(input("Enter amount to deposit: "))
                    balance += deposit_amount
                    print(f"You have deposited ₹{deposit_amount}")
                    print("Updated balance: ₹", balance, "\n")

                elif option == 4:
                    print("You have successfully exited. Please remove your card\n")
                    break

                else:
                    print("Invalid option\n")

            break  
        else:
            attempts += 1
            print(f" Invalid PIN. Attempts left: {3 - attempts}\n")

    if attempts == 3:
        print(" Too many wrong attempts. Your card is blocked!")

else:
    print("Invalid card, please remove")
