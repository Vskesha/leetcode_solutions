from functools import wraps
from typing import List


class CustomFunction:
    """
    Returns f(x, y) for any given positive integers x and y.
    Note that f(x, y) is increasing with respect to both x and y.
    i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    """

    functions = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        3: lambda x, y: x**2 + y,
        4: lambda x, y: x + y**2,
        5: lambda x, y: x**2 + y**2,
        6: lambda x, y: (x + y) ** 2,
        7: lambda x, y: x**3 + y**3,
        8: lambda x, y: x**2 * y,
        9: lambda x, y: x * y**2,
    }

    def __init__(self, function_id: int):
        self.function_id = function_id

    def f(self, x, y):
        return CustomFunction.functions[self.function_id](x, y)


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def findSolution(self, function_id: int, z: int) -> List[List[int]]:
            custom_function = CustomFunction(function_id)
            return self.original.findSolution(customfunction=custom_function, z=z)

    return Wrapper


@sol_decorator
class Solution:
    def findSolution(self, customfunction: "CustomFunction", z: int) -> List[List[int]]:
        x = 1
        y = z
        res = []
        while x <= z and y > 0:
            mid = customfunction.f(x, y)
            if mid == z:
                res.append([x, y])
                x += 1
                y -= 1
            elif mid < z:
                x += 1
            else:
                y -= 1
        return res


def test_find_solution():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.findSolution(function_id=1, z=4) == [[1, 3], [2, 2], [3, 1]]  # noqa
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.findSolution(function_id=2, z=5) == [[1, 5], [5, 1]]  # noqa
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.findSolution(function_id=3, z=10) == [[1, 9], [2, 6], [3, 1]]  # noqa
    print("OK")

    print("Test 4 ... ", end="")
    assert sol.findSolution(function_id=4, z=10) == [[1, 3], [6, 2], [9, 1]]  # noqa
    print("OK")

    print("Test 5 ... ", end="")
    assert sol.findSolution(function_id=5, z=50) == [[1, 7], [5, 5], [7, 1]]  # noqa
    print("OK")

    print("Test 6 ... ", end="")
    assert sol.findSolution(function_id=6, z=16) == [[1, 3], [2, 2], [3, 1]]  # noqa
    print("OK")

    print("Test 7 ... ", end="")
    assert sol.findSolution(function_id=7, z=72) == [[2, 4], [4, 2]]  # noqa
    print("OK")

    print("Test 8 ... ", end="")
    assert sol.findSolution(function_id=8, z=32) == [[1, 32], [2, 8], [4, 2]]  # noqa
    print("OK")

    print("Test 9 ... ", end="")
    assert sol.findSolution(function_id=9, z=32) == [[2, 4], [8, 2], [32, 1]]  # noqa
    print("OK")


if __name__ == "__main__":
    test_find_solution()
