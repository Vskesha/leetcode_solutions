import unittest

from leetcode_solutions._test_meta import TestMeta


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType]:
            self.spaces[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    null, true, false = None, True, False
    test_cases = [
        {
            "class": ParkingSystem,
            "cls_init_args": [1, 1, 0],
            "class_methods": ["addCar", "addCar", "addCar", "addCar"],
            "args": [[1], [2], [3], [1]],
            "expected": [true, true, false, false],
        },
    ]


if __name__ == "__main__":
    unittest.main()
