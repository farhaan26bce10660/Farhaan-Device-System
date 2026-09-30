from validation import get_number, get_integer


def apply_operation(left, operator, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError
        return left / right
    raise ValueError("Invalid operator")


def evaluate_expression(numbers, operators):
    if not numbers:
        return 0
    values = [numbers[0]]
    low_precedence_ops = []
    for operator, number in zip(operators, numbers[1:]):
        if operator == "*":
            values[-1] = apply_operation(values[-1], "*", number)
        elif operator == "/":
            values[-1] = apply_operation(values[-1], "/", number)
        else:
            low_precedence_ops.append(operator)
            values.append(number)
    result = values[0]
    for operator, value in zip(low_precedence_ops, values[1:]):
        result = apply_operation(result, operator, value)
    return result


def calculator():
    numbers = [get_number("\nWhat is your number : ")]
    operators = []
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Result")
        print("6. Restart")
        print("7. Exit")
        operation = get_integer("What operation do you want to perform (1/2/3/4/5/6/7): ")
        if operation in (1, 2, 3, 4):
            number = get_number("What is the next number : ")
            if operation == 4 and number == 0:
                print("Cannot divide by zero!")
                continue
            operators.append({1: "+", 2: "-", 3: "*", 4: "/"}[operation])
            numbers.append(number)
        elif operation == 5:
            try:
                print("Result =", evaluate_expression(numbers, operators))
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")
        elif operation == 6:
            numbers = [get_number("\nWhat is your number : ")]
            operators = []
            print("Calculator restarted.")
        elif operation == 7:
            print("Exiting calculator...")
            break
        else:
            print("Invalid operation number!!!")
