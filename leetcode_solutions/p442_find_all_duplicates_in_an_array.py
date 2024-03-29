from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        for n in nums:
            if n in seen:
                seen.remove(n)
                ans.append(n)
            else:
                seen.add(n)
        return ans


def test_find_duplicates():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert set(sol.findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1])) == {2, 3}
    print("OK")

    print("Test 2 ... ", end="")
    assert set(sol.findDuplicates(nums=[1, 1, 2])) == {1}
    print("OK")

    print("Test 3 ... ", end="")
    assert set(sol.findDuplicates(nums=[1])) == set()
    print("OK")


if __name__ == "__main__":
    test_find_duplicates()
