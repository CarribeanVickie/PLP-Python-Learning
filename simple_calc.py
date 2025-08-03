number1 = float(input("Input the first number...."))
number2 = float(input("Input the second number...."))

operation = input("Enter operation to be performed...")

if operation == "+":
    result = number1 + number2
    print("Sum of Number 1 and Number 2: ", result)
elif operation == "-":
    result = number1 - number2
    print("Difference of Number 1 and number 2: ", result)
elif operation == "*":
    result = number1 * number2
    print("Multiplication of number 1 and number 2: ", result)
elif operation == "/":
    if number2 == 0:
        print("Cannot divide by Zero")
    else:
        result = number1 / number2
        print("Division of number 1 and number 2: ", result)
else:
    print("Choose one of the following operations: +, -, *, / ")