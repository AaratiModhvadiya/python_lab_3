class Calculator:
    def __init__(self):
        self.__result = 0  # Private attribute to store the result

    def add(self, value):
        """Add a value to the current result."""
        self.__result += value
        return self.__result

    def subtract(self, value):
        """Subtract a value from the current result."""
        self.__result -= value
        return self.__result

    def get_result(self):
        """Return the current result."""
        return self.__result

    def reset(self):
        """Reset the result to zero."""
        self.__result = 0

# Example usage
calc = Calculator()

print("Initial result:", calc.get_result())

# Performing addition
print("Adding 10:", calc.add(10))
print("Adding 5:", calc.add(5))

# Performing subtraction
print("Subtracting 3:", calc.subtract(3))
print("Subtracting 2:", calc.subtract(2))

# Get final result
print("Final result:", calc.get_result())

# Resetting the calculator
calc.reset()
print("Result after reset:", calc.get_result())
