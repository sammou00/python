class Calculator:
    """_summary_
    This class is a simple calculator program that takes two numbers and an operator
    as input and returns the result of the operation.
    """

    def get_number(self):
        while True:
            try:
                num = float(input("Enter a number: "))
                return num
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_operator(self):
        valid_operations = ['+', '-', '*', '/']
        while True:
            operation = input("Enter an operation (+, -, *, /): ")
            if operation in valid_operations:
                return operation
            else:
                print("Invalid input. Please enter a valid operation.")

    def calculate(self, num_1, operation, num_2):
        try:
            if operation == '+':
                return num_1 + num_2
            elif operation == '-':
                return num_1 - num_2
            elif operation == '*':
                return num_1 * num_2
            elif operation == '/':
                if num_2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return num_1 / num_2
        except ZeroDivisionError as e:
            return str(e)
        except Exception as e:
            return f"An error occurred: {e}"

    def start(self):
        print("Welcome to calculator.")
        while True:
            num_1 = self.get_number()
            operation = self.get_operator()
            num_2 = self.get_number()
            result = self.calculate(num_1, operation, num_2)
            print(f"{num_1} {operation} {num_2} = {result}")

            answer = input("Would you like to perform another calculation? (y/n): ").strip().lower()
            if answer != 'y':
                print("Thank you for using calculator.")
                break

if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()
