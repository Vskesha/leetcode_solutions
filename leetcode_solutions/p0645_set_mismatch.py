from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        al = set(range(1, len(nums) + 1))
        ans = []
        for n in nums:
            if n in al:
                al.remove(n)
            else:
                ans.append(n)
        ans.append(al.pop())
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findErrorNums(nums=[1, 2, 2, 4]) == [2, 3]
    print("OK")

    print("Test 2... ", end="")
    assert sol.findErrorNums(nums=[1, 1]) == [1, 2]
    print("OK")


if __name__ == "__main__":
    test()
