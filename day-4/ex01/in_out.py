def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:

    def inner() -> float:
        """
        Execute the provided function, update the value, and return the result.

        This inner function performs the following steps:
        1. Execute the provided function using the current input value.
        2. Update the input value with the result of the calculation.
        3. Increment the internal counter to keep track of the number of calls.
        4. Return the result of the calculation.

        Nonlocal:
        Used to modify a variable in the nearest enclosing scope that's
        not the global scope. It allows you to work with variables from
        a parent (enclosing) function's scope.

        Returns:
        float: The result of the calculation performed by the provided function
        """
        nonlocal x
        result = function(x)
        x = result
        return result
    return inner
