# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform safe division with error handling.

    Args:
        numerator: The numerator (string or number).
        denominator: The denominator (string or number).

    Returns:
        str: Result of division or error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is{result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
