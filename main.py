from loadwallet import LoadWallet

def read_amount(prompt):
    while True:
        value = input(prompt).strip().upper().replace(",", "")
        if value.startswith("P"):
            value = value[1:].strip()

        try:
            amount = float(value)
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid amount, for example P50.")


def main():
    owner = input("Enter owner name: ")
    mobile_number = input("Enter mobile number: ")
    starting_balance = read_amount("Enter starting balance: ")
    wallet = LoadWallet(owner, mobile_number, starting_balance)

    while True:
        print("\n----- MENU -----")
        print("1. Top Up Load")
        print("2. Send Load (same network)")
        print("3. Send Load (other network, with fee)")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()
        if choice == "1":
            wallet.top_up(read_amount("Enter top-up amount: "))
        elif choice == "2":
            recipient_number = input("Enter recipient mobile number: ")
            amount = read_amount("Enter load amount: ")
            wallet.send_load(recipient_number, amount)
        elif choice == "3":
            recipient_number = input("Enter recipient mobile number: ")
            amount = read_amount("Enter load amount: ")
            fee = read_amount("Enter service fee: ")
            wallet.send_with_fee(recipient_number, amount, fee)
        elif choice == "4":
            wallet.show_balance()
        elif choice == "5":
            print("Thank you for using the Load Wallet.")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
