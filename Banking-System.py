#Define class and its relevant objects
class BankAccount:
    def __init__(self, account_number, owner, pin, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.pin = pin
        self.balance = balance
        
 #Function to deposite money to bank account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    #Function to withdraw money from bank account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    #Function to check balance in bank account
    def check_balance(self):
        print(f"{self.owner}'s Balance: ${self.balance}")

    def to_line(self):
        return f"{self.account_number},{self.owner},{self.pin},{self.balance}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        return BankAccount(int(parts[0]), parts[1], parts[2], float(parts[3]))

#Create a class to create account, save data and for authentication using functions 
class BankSystem:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.next_account_number = 1001
        self.filename = filename
        self.load_data()

    def create_account(self, owner, pin):
        acc_num = self.next_account_number
        self.accounts[acc_num] = BankAccount(acc_num, owner, pin)
        self.next_account_number += 1
        self.save_data()
        print(f"Account created successfully! Your account number is {acc_num}")

    def authenticate(self, acc_num, pin):
        account = self.accounts.get(acc_num)
        if account and account.pin == pin:
            print(f"Welcome back, {account.owner}!")
            return account
        else:
            print("Authentication failed.")
            return None

    def save_data(self):
        with open(self.filename, "w") as file:
            for account in self.accounts.values():
                file.write(account.to_line())

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    account = BankAccount.from_line(line)
                    self.accounts[account.account_number] = account
                    if account.account_number >= self.next_account_number:
                        self.next_account_number = account.account_number + 1
        except FileNotFoundError:
            pass

#Home screen to create, login or exit bank account
def main():
    bank = BankSystem()
    print("Welcome to PPH Bank!")

    while True:
        print("\nMain Menu")
        print("1. Create Account Number")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            while True:
                pin = input("Set a 4-digit PIN: ")
                if pin.isdigit() and len(pin) == 4:
                    break
                else:
                    print("PIN must be exactly 4 digits.")
            bank.create_account(name, pin)

        elif choice == '2':
            try:
                acc_num = int(input("Enter account number: "))
                pin = input("Enter PIN: ")
                account = bank.authenticate(acc_num, pin)

                #After login, you can either deposit, withdraw, check balance or logout
                if account:
                    while True:
                        print("\nAccount Menu")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Logout")

                        action = input("Select an action: ")

                        if action == '1':
                            amount = float(input("Enter deposit amount: "))
                            account.deposit(amount)
                            bank.save_data()
                        elif action == '2':
                            amount = float(input("Enter withdrawal amount: "))
                            account.withdraw(amount)
                            bank.save_data()
                        elif action == '3':
                            account.check_balance()
                        elif action == '4':
                            print("You have been logged out.")
                            break
                        else:
                            print("Invalid choice.")
            except ValueError:
                print("Invalid account number.")

        elif choice == '3':
            print("Thank you for using PPH Bank!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
