print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
choice = input("Enter operation: ")

if choice == "+":
    print("Result:", num1 + num2)
elif choice == "-":
    print("Result:", num1 - num2)
elif choice == "*":
    print("Result:", num1 * num2)
elif choice == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")
