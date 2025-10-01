# calculator_safe.py
# Simple Calculator with error handling and friendly user prompts

def add(a, b):
    """Return a + b"""
    return a + b

def subtract(a, b):
    """Return a - b"""
    return a - b

def multiply(a, b):
    """Return a * b"""
    return a * b

def divide(a, b):
    """Return a / b (raises ZeroDivisionError if b == 0)"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """
    Ask the user for a number until they give a valid one.
    If the user types 'q' it returns None (used as cancel).
    """
    while True:
        text = input(prompt).strip()
        if text.lower() in ("q", "quit", "exit"):
            return None
        try:
            value = float(text)
            return value
        except ValueError:
            print("Please enter a valid number (or 'q' to cancel).")


def main():
    print("=== Simple Calculator (type 'q' any time to cancel) ===")

    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter choice (1-5): ").strip().lower()

        # allow 'q' or '5' to quit
        if choice in ("5", "q", "quit", "exit"):
            print("Goodbye! 👋")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            continue

        # get two numbers from the user (or allow cancellation)
        a = get_number("Enter the first number: ")
        if a is None:
            print("Operation cancelled.")
            continue

        b = get_number("Enter the second number: ")
        if b is None:
            print("Operation cancelled.")
            continue

        # perform the chosen operation with exception handling
        try:
            if choice == "1":
                result = add(a, b)
                op = "+"
            elif choice == "2":
                result = subtract(a, b)
                op = "-"
            elif choice == "3":
                result = multiply(a, b)
                op = "*"
            elif choice == "4":
                result = divide(a, b)
                op = "/"

            # Print result. Use formatting to show floats nicely.
            print(f"{a} {op} {b} = {result}")

        except ZeroDivisionError:
            # Specific helpful message for division by zero
            print("Error: You cannot divide by zero. Try a different second number.")
        except Exception as e:
            # Catch any other unexpected error so the program doesn't crash
            print("An unexpected error occurred:", str(e))


if __name__ == "__main__":
    main()
