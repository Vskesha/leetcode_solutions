from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        seen = set()
        for n in nums:
            if n in seen:
                ans = max(ans, abs(n))
            else:
                seen.add(-n)
        return ans


def test_find_max_k():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findMaxK(nums=[-1, 2, -3, 3]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.findMaxK(nums=[-1, 10, 6, 7, -7, 1]) == 7
    print("OK")

    print("Test 3... ", end="")
    assert sol.findMaxK(nums=[-10, 8, 6, 7, -2, -3]) == -1
    print("OK")


if __name__ == "__main__":
    test_find_max_k()
