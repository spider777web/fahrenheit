def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("Temperature Converter")
print("1. Fahrenheit to Celsius")

choice = input("Choose an option: ")

if choice == "1":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius:.2f}°C")

else:
    print("Invalid option")
