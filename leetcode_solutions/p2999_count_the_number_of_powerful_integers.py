import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    ) -> int:
        tofinish = self.num_pow(finish, limit, s)
        tostart = self.num_pow(start - 1, limit, s)
        return tofinish - tostart

    def num_pow(self, finish: int, limit: int, s: str):
        finish = str(finish)
        lf, ls = len(finish), len(s)

        if lf < ls:
            return 0
        if lf == ls:
            return int(finish >= s)

        ans = 0
        for di in range(lf, ls, -1):
            df = int(finish[-di])
            if df > limit:
                ans += pow(limit + 1, di - ls)
                break
            ans += df * pow(limit + 1, di - ls - 1)
        else:
            ans += int(finish[-ls:] >= s)

        return ans


class Solution2:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    ) -> int:
        sfinish, sstart = str(finish), str(start)
        tofinish = self.num_pow(sfinish, limit, s)
        tostart = self.num_pow(sstart, limit, s)
        additional = sstart.endswith(s) and all(
            int(d) <= limit for d in sstart
        )
        ans = tofinish - tostart + additional
        return ans

    def num_pow(self, finish: str, limit: int, s: str):
        lf, ls = len(finish), len(s)

        if lf < ls:
            return 0
        if lf == ls:
            return int(finish >= s)

        ans = 0
        for di in range(lf, ls, -1):
            df = int(finish[-di])
            if df > limit:
                ans += pow(limit + 1, di - ls)
                break
            ans += df * pow(limit + 1, di - ls - 1)
        else:
            ans += int(finish[-ls:] >= s)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfPowerfulInt"] * 5,
            "kwargs": [
                dict(start=1, finish=6000, limit=4, s="124"),
                dict(start=15, finish=215, limit=6, s="10"),
                dict(start=1000, finish=2000, limit=4, s="3000"),
                dict(start=1, finish=971, limit=9, s="72"),
                dict(
                    start=63935267123, finish=334359420935946, limit=6, s="3"
                ),
            ],
            "expected": [5, 2, 0, 9, 340924566339],
        },
    ]


if __name__ == "__main__":
    unittest.main()
