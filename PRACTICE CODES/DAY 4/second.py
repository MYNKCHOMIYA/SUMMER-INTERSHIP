#Error& Exceptional handling
n1 = int(input("Enter first number: "))
try:
        y = 25/n1
        print(y)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")


