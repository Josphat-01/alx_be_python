FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0
FREEZING_POINT_F = 32.0

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FREEZING_POINT_F
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FREEZING_POINT_F
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F

if __name__ == "__main__":
    try:
        temp_str = input("Enter the temperature value: ").strip()
        if not temp_str.replace('.', '', 1).lstrip('-').isdigit():
            raise ValueError("Invalid temperature. Enter numeric value")

        temp_value = float(temp_str)
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted:.2f}°F")
        elif unit == "F":
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print(e)