# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Does not access class or instance.
        Simply returns the sum of two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Has access to the class (cls).
        Prints the class attribute and performs multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demo usage
if __name__ == "__main__":
    # Using the static method
    result_add = Calculator.add(10, 5)
    print(f"Addition result: {result_add}")

    # Using the class method
    result_multiply = Calculator.multiply(10, 5)
    print(f"Multiplication result: {result_multiply}")
