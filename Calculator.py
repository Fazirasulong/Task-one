def calculator():
    while True:
        print("Simple Calculator!")
        try:
            num1 = float(input("Enter the first number:"))
            operation = input("Enter an operation (+, -, *, /):")
            num2 = float(input("Enter the second number:"))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed")
                    continue
            else:
                print("Invalid operation Please try again")
                continue

            print(f"The result is:{result}")
        except ValueError:
            print("Invalid input Please enter valid numbers")
            continue

        again = input("Do you want to make another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

calculator()