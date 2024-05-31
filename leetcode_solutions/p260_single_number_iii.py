from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(lambda x, y: x ^ y, nums)

        sb = 1
        while not sb & x:
            sb <<= 1

        n1 = n2 = 0
        for n in nums:
            if n & sb:
                n1 ^= n
            else:
                n2 ^= n

        return [n1, n2]


class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        single = set()

        for n in nums:
            if n in single:
                single.remove(n)
            else:
                single.add(n)

        return list(single)


def test_single_number():
    solution = Solution()

    print("Test 1... ", end="")
    assert set(solution.singleNumber(nums=[1, 2, 1, 3, 2, 5])) == {3, 5}
    print("OK")

    print("Test 2... ", end="")
    assert set(solution.singleNumber(nums=[-1, 0])) == {-1, 0}
    print("OK")

    print("Test 3... ", end="")
    assert set(solution.singleNumber(nums=[0, 1])) == {1, 0}
    print("OK")


if __name__ == "__main__":
    test_single_number()
