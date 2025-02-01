import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bc = num2.bit_count()
        n1 = bin(num1)[2:]
        ln = len(n1)

        bits = []

        for i, b in enumerate(n1):
            left = ln - i
            if bc and bc < left:
                bits.append(b)
                bc -= int(b)
            else:
                bits.extend(["1" if bc else "0"] * max(left, bc))
                break

        ans = "".join(bits)
        ans = int(ans, 2)
        return ans


class Solution2:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bc = num2.bit_count()
        bits = list(bin(num1)[2:])
        if bc >= len(bits):
            return int("1" * bc, 2)
        d = num1.bit_count() - bc
        i = len(bits) - 1
        while d > 0:
            if bits[i] == "1":
                d -= 1
                bits[i] = "0"
            i -= 1
        while d < 0:
            if bits[i] == "0":
                d += 1
                bits[i] = "1"
            i -= 1
        return int("".join(bits), 2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimizeXor"] * 3,
            "kwargs": [
                dict(num1=25, num2=72),
                dict(num1=3, num2=5),
                dict(num1=1, num2=12),
            ],
            "expected": [24, 3, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
