num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    case _:
        result = "Error: Invalid operation"
print(f"The result is: {result}")