from operations import add, subtract, multiply, divide

def calculator():
    print("Welcome to the calculator!")
    print("Here are the available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Please choose an operation: ")
    if operation not in ["1", "2", "3", "4"]:
        print("Invalid operation.")
        return
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if operation == "1":
        print(add(a, b))
    elif operation == "2":
        print(subtract(a, b))
    elif operation == "3":
        print(multiply(a, b))
    elif operation == "4":
        print(divide(a, b))
        
if __name__ == "__main__":
    calculator()