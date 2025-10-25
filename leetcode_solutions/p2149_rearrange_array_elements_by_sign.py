from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        pi, ni = 0, 1
        ans = [0] * ln
        for n in nums:
            if n > 0:
                ans[pi] = n
                pi += 2
            else:
                ans[ni] = n
                ni += 2
        return ans


class Solution2:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def positive(nums):
            for n in nums:
                if n > 0:
                    yield n

        def negative(nums):
            for n in nums:
                if n < 0:
                    yield n

        pos = positive(nums)
        neg = negative(nums)
        return [next(neg) if i % 2 else next(pos) for i in range(len(nums))]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.rearrangeArray(nums=[3, 1, -2, -5, 2, -4]) == [
        3,
        -2,
        1,
        -5,
        2,
        -4,
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.rearrangeArray(nums=[-1, 1]) == [1, -1]
    print("OK")


if __name__ == "__main__":
    test()
