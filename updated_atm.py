VALID_CARDS = ['sbi', 'icici', 'hdfc', 'axis']
VALID_PIN = "1234"
MAX_ATTEMPTS = 3

balance = 0
card = input("Insert a card: ").strip().lower()

if card in VALID_CARDS:
    print("----------WELCOME TO ATM------------")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        pin = input("Enter your PIN: ")

        if pin == VALID_PIN:
            
            while True:
                print("\n*********************")
                print("Choose an option: ")
                print("1. Check Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Exit")
                print("*********************")

                try:
                    option = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")
                    continue

                if option == 1:
                    print("Your balance is: ₹", balance)

                elif option == 2:
                    if balance == 0:
                        print("Zero balance, please deposit first...")
                    else:
                        try:
                            withdraw_amount = int(input("Enter amount to withdraw: "))
                            if withdraw_amount <= 0:
                                print("Amount must be greater than zero.")
                            elif withdraw_amount <= balance:
                                balance -= withdraw_amount
                                print(f"You have withdrawn ₹{withdraw_amount}")
                                print("Remaining balance: ₹", balance)
                            else:
                                print("Insufficient balance")
                        except ValueError:
                            print("Please enter a valid amount.")

                elif option == 3:
                    try:
                        deposit_amount = int(input("Enter amount to deposit: "))
                        if deposit_amount <= 0:
                            print("Amount must be greater than zero.")
                        else:
                            balance += deposit_amount
                            print(f"You have deposited ₹{deposit_amount}")
                            print("Updated balance: ₹", balance)
                    except ValueError:
                        print("Please enter a valid amount.")

                elif option == 4:
                    print("You have successfully exited. Please remove your card.")
                    break

                else:
                    print("Invalid option. Please select between 1 and 4.")
            break  
        else:
            attempts += 1
            if attempts < MAX_ATTEMPTS:
                print(f"Invalid PIN. Attempts remaining: {MAX_ATTEMPTS - attempts}")
            else:
                print("Card blocked due to multiple incorrect PIN attempts.")
else:
    print("Invalid card")
