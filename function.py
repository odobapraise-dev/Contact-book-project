balance = 0

def deposit(balance, amount):
    balance += amount
    print(f"Deposited {amount}. New balance = {balance}")
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Not enough funds!")
    else:
        balance -= amount
        print(f"Withdrew {amount}. New balance = {balance}")
    return balance

def check_balance(balance):
    print(f"Your current balance = {balance}")
    return balance

# menu options
options = {
    1: 'deposit',
    2: 'withdraw',
    3: 'check_balance',
    4: 'quit'
}

# main loop
while True:
    print("\n---- ATM ----")
    for number, value in options.items():
        print(f"{number}. {value}")

    choice = int(input("Pick an option: "))

    if choice == 1:   # deposit
        amount = int(input("Enter deposit amount: "))
        balance = deposit(balance, amount)

    elif choice == 2:   # withdraw
        amount = int(input("Enter withdrawal amount: "))
        balance = withdraw(balance, amount)

    elif choice == 3:   # check balance
        balance = check_balance(balance)

    elif choice == 4:   # quit
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid option. Try again!")
