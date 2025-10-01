# -----------------------------
# Banking App (OOP Project)
# -----------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance = {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance = {self.balance}")

    def check_balance(self):
        print(f"Current Balance = {self.balance}")


# -----------------------------
# Main Program
# -----------------------------
def main():
    print("Welcome to the Banking App")
    name = input("Enter account holder's name: ")
    account = BankAccount(name)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using the Banking App.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
