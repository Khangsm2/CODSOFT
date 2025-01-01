def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # User selects operation
            choice = input("Enter choice (1/2/3/4 or 'q' to quit): ").strip()
            if choice.lower() == 'q':
                print("Exiting calculator. Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid input. Please select a valid option.")
                continue

            # Get user input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result is: {num1 / num2}")

        except ValueError:
            print("Invalid input. Please enter numerical values.")

# Run the calculator
calculator()
