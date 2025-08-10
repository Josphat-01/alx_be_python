from arithmetic_operations import perform_operation
from fns_and_dsa.arithmetic_operations import perform_operation

if __name__ == "__main__":
    print("Arithmetic Operations")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation(add, subtract, multiply, divide): ").strip().lower()

        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
