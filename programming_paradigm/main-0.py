from bank_account import BankAccount

def main():
    account = BankAccount(100)
    print("Welcome to the Simple Bank Account Program!")
    print("Available commands: deposit, withdraw, display, exit")

    while True:
        command = input("Enter a command (deposit, withdraw, display, exit): ").strip().lower()
        
        if command == "deposit":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif command == "withdraw":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif command == "display":
            print(f"Current Balance: ${account.display_balance():.2f}")
        elif command == "exit":
            print("Thank you for using the Simple Bank Account Program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

