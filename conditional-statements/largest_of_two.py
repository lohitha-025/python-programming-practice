num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Largest number:", num1)
elif num2 > num1:
    print("Largest number:", num2)
else:
    print("Both numbers are equal")