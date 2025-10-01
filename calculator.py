# Calculator with functions

# Step 1: Define functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by 0."
    return a / b


# Step 2: Create the menu
operations = {
    1: "Add",
    2: "Subtract",
    3: "Multiply",
    4: "Divide",
    5: "Quit"
}

# Step 3: Loop for multiple calculations
while True:
    print("\n--- Calculator ---")
    for number, name in operations.items():
        print(f"{number}. {name}")

    choice = int(input("Choose an operation: "))

    if choice == 5:
        print("Goodbye!")
        break

    if choice in [1, 2, 3, 4]:  # valid choices
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print(f"Result = {add(a, b)}")
        elif choice == 2:
            print(f"Result = {subtract(a, b)}")
        elif choice == 3:
            print(f"Result = {multiply(a, b)}")
        elif choice == 4:
            print(f"Result = {divide(a, b)}")
    else:
        print("Invalid option, try again.")
