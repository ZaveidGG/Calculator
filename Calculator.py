from art import logo

def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

def printSymbols():
    for operand in operations:
        print(operand)
    symbol = input("Pick an operation to do:")

    if symbol not in operations:
        print("You have entered an invalid option!")


    return symbol

def compute(symbol,num1,num2):
    function = operations[symbol]
    answer = function(num1, num2)

    return answer

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    pickAnother = True
    num1 = float(input("Enter first number:\n"))
    symbol = printSymbols()
    num2 = float(input("Enter second number:\n"))
    answer = compute(symbol,num1,num2)
    print(print(f"{num1} {symbol} {num2} = {answer}"))

    while pickAnother:
        choice = input("Continue computation with another number? Type 'y' or 'n'")
        if choice == 'y':
            pickAnother = True
            symbol = printSymbols()
            num3 = float(input("Enter another number:"))
            newAnswer = compute(symbol,answer,num3)
            print(f"{answer} {symbol} {num3} = {newAnswer}")
        elif choice == 'n':
            pickAnother = False
            calculator()
        else:
            print("You have entered an invalid option!")
            pickAnother = False


calculator()