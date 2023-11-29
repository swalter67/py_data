from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            try:
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    print(f"Error: {function} call too many times")
            except AssertionError as e:
                print("Error:", e)
        return limit_function

    return callLimiter
