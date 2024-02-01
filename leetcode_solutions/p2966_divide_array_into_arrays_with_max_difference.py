from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        ans = []
        for i in range(0, ln, 3):
            if nums[i] + k >= nums[i + 2]:
                ans.append(nums[i : i + 3])
            else:
                return []
        return ans


def test_diff(arr: List[List[int]], k: int) -> bool:
    for sarr in arr:
        if max(sarr) - min(sarr) > k:
            return False
    return True


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert test_diff(sol.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2), k=2)
    print("OK")

    print("Test 2... ", end="")
    assert test_diff(sol.divideArray(nums=[1, 3, 3, 2, 7, 3], k=3), k=3)
    print("OK")


if __name__ == "__main__":
    test()
