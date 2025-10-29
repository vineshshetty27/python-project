# calculator.py
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("What kind of operation do you want to perform?")
    print("Press + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")

    op = input("Enter the operator: ")

    match op:
        case '+':
            print(f"The result is: {a + b}")
        case '-':
            print(f"The result is: {a - b}")
        case '*':
            print(f"The result is: {a * b}")
        case '/':
            print(f"The result is: {a / b}")
        case _:
            print("Invalid operator entered")

except Exception as e:
    print("Enter valid values of a and b")
