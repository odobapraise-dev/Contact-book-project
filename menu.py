# --- Menu Ordering System ---

# Step 1: Define menu items (dictionary)
menu = {
    1: ('burger', 1500),
    2: ('pizza', 3000),
    3: ('fries', 1000),
    4: ('drink', 500)
}

# Step 2: Total bill starts from 0
total = 0

# Step 3: Infinite loop to take orders
while True:
    print("\n--- Menu ---")
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - {price}")
    print("0. Finish order")

    choice = int(input("Enter the number of the item you want: "))

    if choice == 0:
        break
    elif choice in menu:
        item, price = menu[choice]
        total += price
        print(f"Added {item} - {price}. Your total = {total}")
    else:
        print("Invalid choice!")

# Step 4: Show final bill
print(f"\nYour total bill is: {total}")
