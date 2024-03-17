from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            s = str(n)
            s = max(s) * len(s)
            ans += int(s)
        return ans


def test_sum_of_encrypted_int():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.sumOfEncryptedInt(nums=[1, 2, 3]) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.sumOfEncryptedInt(nums=[10, 21, 31]) == 66
    print("OK")


if __name__ == "__main__":
    test_sum_of_encrypted_int()
