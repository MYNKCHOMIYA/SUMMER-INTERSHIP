# SIMPLE CALCULATOR
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %): ")
if operation == '+':
    result = A + B
elif operation == '-':
    result = A - B
elif operation == '*':
    result = A * B
elif operation == '/':
    if B != 0:
        result = A / B
    else:
        result = "Error: Division by zero is not allowed."
elif operation == '%':
    if B != 0:
        result = A % B
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."
print(f"The result of {A} {operation} {B} is: {result}")
