# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-final-newline

import time
import math
from typing import Callable, Any


def timed(function: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start: float = time.time()
        value = function(*args, **kwargs)
        end: float = time.time()

        elapsed_time = (end - start) * 1000

        print(f"Function {function.__name__} took {elapsed_time:.2f} ms")
        return value

    return wrapper


# sample usage of timed decorator
@timed
def factorial(x: int) -> int:
    return math.factorial(x)

factorial(1000)
