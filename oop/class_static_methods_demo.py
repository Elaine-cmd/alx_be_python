"""
This module demonstrates the use of class and static methods in Python.
"""

class Calculator:
    """
    A class that provides basic arithmetic operations using
    class and static methods.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Adds two numbers together. This is a static method as it does not
        depend on the class or instance state.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Multiplies two numbers together. This is a class method that
        accesses a class attribute before performing the calculation.

        Args:
            cls: The class itself, passed implicitly.
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b