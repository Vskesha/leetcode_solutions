import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return 1

        snums = sorted(nums)
        ans = 0
        for d in range(1, int(ln**0.5) + 1):
            if ln % d:
                continue
            for k in {d, ln // d}:
                for i in range(0, ln, k):
                    sti = i
                    for j in range(i + 1, i + k):
                        if nums[j] < nums[j - 1]:
                            sti = j
                            break
                    if snums[i : i + k] != nums[sti : i + k] + nums[i:sti]:
                        break
                else:
                    ans += k

        return ans


class Solution2:
    def sortableIntegers(self, nums: list[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return 1

        snums = sorted(nums)

        ans = int(nums == snums)

        for d in range(2, int(ln**0.5) + 1):
            if ln % d:
                continue
            for k in {d, ln // d}:
                for i in range(0, ln, k):
                    sti = i
                    for j in range(i + 1, i + k):
                        if nums[j] < nums[j - 1]:
                            sti = j
                            break
                    if snums[i : i + k] != nums[sti : i + k] + nums[i:sti]:
                        break
                else:
                    ans += k

        sti = 0
        for j in range(1, ln):
            if nums[j] < nums[j - 1]:
                sti = j
                break
        if snums == nums[sti:] + nums[:sti]:
            ans += ln

        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sortableIntegers"] * 4,
            "kwargs": [
                dict(nums=[1, 2, 3, 4, 5, 6]),
                dict(nums=[3, 1, 2]),
                dict(nums=[7, 6, 5]),
                dict(nums=[5, 8]),
            ],
            "expected": [12, 3, 0, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
