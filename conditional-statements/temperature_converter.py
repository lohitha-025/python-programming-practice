print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice (1-4): "))

temperature = float(input("Enter the temperature: "))

if choice == 1:
    result = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit:", result)

elif choice == 2:
    result = (temperature - 32) * 5/9
    print("Temperature in Celsius:", result)

elif choice == 3:
    result = temperature + 273.15
    print("Temperature in Kelvin:", result)

elif choice == 4:
    result = temperature - 273.15
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice")