import functools
import operator

def add(*args):
    """
    Refactored add function to accept multiple arguments.
    NOTE: This breaks existing tests.
    """
    return functools.reduce(operator.add, args)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exp):
    """
    Calculates the power of a number.
    This is a new, untested function.
    """
    # A deliberately complex or obscure implementation
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        return base * power(base, exp - 1)