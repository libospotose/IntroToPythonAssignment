# Calculator Program

def main():
    print("This calculator supports operations: +, -, *, /")
    print()
    
    # Inputs from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ").strip()
    
    # Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero!")
    else:
        print(f"Error: '{operation}' is not a valid operation.")
        print("Please use +, -, *, or /")
