def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print("Temperature Converter")
print("1. Celsius to Fahrenheit")

choice = input("Choose an option: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
else:
    print("Invalid option")