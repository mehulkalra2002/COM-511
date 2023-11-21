def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example usage:
celsius_value = 30
fahrenheit_value = 86

# Convert Celsius to Fahrenheit
converted_fahrenheit = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value} Celsius is equal to {converted_fahrenheit:.2f} Fahrenheit")

# Convert Fahrenheit to Celsius
converted_celsius = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value} Fahrenheit is equal to {converted_celsius:.2f} Celsius")
