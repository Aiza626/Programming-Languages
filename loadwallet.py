class LoadWallet:

    def __init__(self, owner, mobile_number, balance):
        self.owner = owner
        self.mobile_number = mobile_number
        self.balance = balance

    def top_up(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self.balance += amount
        print(f"New balance: P{self.balance:.2f}")

    def send_load(self, recipient_number, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Load sent to {recipient_number}.")
            print(f"New balance: P{self.balance:.2f}")

    def send_with_fee(self, recipient_number, amount, fee):
        if amount <= 0 or fee < 0:
            print("Enter a valid load amount and service fee.")
            return

        total = amount + fee
        if total > self.balance:
            print("Insufficient balance for the load and service fee.")
            return

        self.balance -= total
        print(f"Load sent to {recipient_number} on another network.")
        print(f"Service fee: P{fee:.2f}")
        print(f"New balance: P{self.balance:.2f}")

    def show_balance(self):
        print(f"Owner         : {self.owner}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self.balance:.2f}")
