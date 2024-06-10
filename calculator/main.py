class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """
    def __init__(self, num1, num2):
        """
        Initialize the calculator with two numbers.
        
        Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        """
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """
        Perform addition.
        
        Returns:
        float: The sum of num1 and num2.
        """
        return self.num1 + self.num2

    def subtract(self):
        """
        Perform subtraction.
        
        Returns:
        float: The difference between num1 and num2.
        """
        return self.num1 - self.num2

    def multiply(self):
        """
        Perform multiplication.
        
        Returns:
        float: The product of num1 and num2.
        """
        return self.num1 * self.num2

    def divide(self):
        """
        Perform division.
        
        Returns:
        float or str: The quotient of num1 divided by num2 or an error message if division by zero is attempted.
        """
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide by zero"

def get_numbers():
    """
    Prompt the user to input two numbers and validate the input.
    
    Returns:
    tuple: A tuple containing two floats.
    """
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    """
    Main function to drive the calculator program. Displays a menu for user to choose an operation
    and processes the user's choice.
    """
    while True:
        # Display the menu
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        try:
            # Prompt the user to choose an operation
            choice = int(input("Enter your choice: "))
        except ValueError:
            # Handle invalid menu choice input
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            # Exit the program if the user chooses option 5
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in [1, 2, 3, 4]:
            # Get numbers from the user for the calculation
            num1, num2 = get_numbers()
            calc = Calculator(num1, num2)

            # Perform the chosen operation and display the result
            if choice == 1:
                print(f"Result: {calc.add()}")
            elif choice == 2:
                print(f"Result: {calc.subtract()}")
            elif choice == 3:
                print(f"Result: {calc.multiply()}")
            elif choice == 4:
                print(f"Result: {calc.divide()}")
        else:
            # Handle invalid operation choice
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
