import unittest
from itertools import groupby

from leetcode_solutions._test_meta import TestMeta


class Solution:
    cnt_n_say = [""] * 31
    cnt_n_say[1] = "1"
    res = []

    for i in range(2, 31):
        for k, gr in groupby(cnt_n_say[i - 1]):
            res.append(str(len(list(gr))))
            res.append(k)
        cnt_n_say[i] = "".join(res)
        res.clear()

    def countAndSay(self, n: int) -> str:
        return self.cnt_n_say[n]


class Solutio2:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            ans = ''.join(f'{len(list(gr))}{el}' for el, gr in groupby(ans))
        return ans


class Solution3:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            aux = [0, ans[0]]
            for d in ans:
                if d == aux[-1]:
                    aux[-2] += 1
                else:
                    aux.extend([1, d])
            ans = ''.join(map(str, aux))
        return ans


class Solution4:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):
            res = []
            counter = 0
            char = ans[0]
            for c in ans:
                if c == char:
                    counter += 1
                else:
                    res.append(f'{counter}{char}')
                    counter = 1
                    char = c
            res.append(f'{counter}{char}')
            ans = ''.join(res)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countAndSay"] * 2,
            "kwargs": [
                dict(n=4),
                dict(n=1),
            ],
            "expected": ["1211", "1"],
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print('Test 1... ', end='')
#     assert sol.countAndSay(n=1) == '1'
#     print('OK')
#
#     print('Test 2... ', end='')
#     assert sol.countAndSay(n=4) == '1211'
#     print('OK')
#
#
# if __name__ == '__main__':
#     test()
