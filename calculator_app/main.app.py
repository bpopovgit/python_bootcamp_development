def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using a dictionary operation.
#answer = operations["*"](4, 8)

def calculator():
    should_accumulate = True
    first_number = float(input("Enter first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation: \"+\", \"-\", \"*\" or \"/\" ")
        second_number = float(input("Enter second number: "))
        calculation = operations[operation_symbol](first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {calculation}")

        user_choice = input(
            f"Type 'y' to continue calculating with {calculation}, or type 'n' to start a new calculation: ")

        if user_choice == 'y':
            first_number = calculation
        else:
            should_accumulate = False
            print("\n" * 20)
            #recursion
            calculator()


calculator()
