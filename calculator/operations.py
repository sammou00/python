def add(a, b):
    """_summary_
    Adds two numbers together.
    """
    return a + b

def subtract(a, b):
    """_summary_
    Subtracts two numbers.
    """
    return a - b


def multiply(a, b):
    """_summary_
    Multiplies two numbers.
    """
    return a * b


def divide(a, b):
    """_summary_
    Divides two numbers.
    """
    if b == 0:
        return "Error: Division by zero."
    return a / b