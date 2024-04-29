from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for n in nums:
            x ^= n
        x = bin(x)[2:].zfill(32)
        k = bin(k)[2:].zfill(32)
        return sum(a != b for a, b in zip(x, k))


class Solution2:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = 0
        for n in nums:
            x ^= n

        res = 0
        while x or k:
            if (x % 2) != (k % 2):
                res += 1
            x //= 2
            k //= 2

        return res


def test_min_operations():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.minOperations(nums=[2, 1, 3, 4], k=1) == 2
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.minOperations(nums=[2, 0, 2, 0], k=0) == 0
    print("OK")

    print("Test 3 ... ", end="")
    assert sol.minOperations(nums=[3, 13, 9, 8, 5, 18, 11, 10], k=13) == 2
    print("OK")


if __name__ == "__main__":
    test_min_operations()
