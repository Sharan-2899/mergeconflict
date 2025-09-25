valid_card = input("Insert a card: ")
balance = 0

if valid_card.lower() in ['sbi', 'icici', 'hdfc', 'axis']:
    print("----------WELCOME TO ATM------------")
    pin = input("Enter your PIN: ")

    if pin == "1234":
        while True:
            print("*********************")
            print("\nChoose an option: ")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")
            print("")
            print("*********************")

            option = int(input("Enter your choice: "))
            print(" ")
            print("*********************")

            if option == 1:
                print("Your balance is: ₹", balance)
                print("")

            elif option == 2:
                if balance <= 0:
                    print("Zero balance, please deposit first...")
                    print(" ")
                else:
                    withdraw_amount = int(input("Enter amount to withdraw: "))
                    if withdraw_amount <= balance:
                        balance -= withdraw_amount
                        print(f"You have withdrawn ₹{withdraw_amount}")
                        print("Remaining balance: ₹", balance)
                    else:
                        print("Insufficient balance")
                        print(" ")

            elif option == 3:
                deposit_amount = int(input("Enter amount to deposit: "))
                balance += deposit_amount
                print(f"You have deposited ₹{deposit_amount}")
                print("Updated balance: ₹", balance)

            elif option == 4:
                print("You have successfully exited. Please remove your card")
                print(" ")
                break 

            else:
                print("Invalid option")  
                print(" ")         
    else:
        print("Invalid PIN")
else:
    print("Invalid card , please remove")
