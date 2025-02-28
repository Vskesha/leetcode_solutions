from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ln, prod, st, ans = len(nums), 1, 0, 0
        for end in range(ln):
            prod *= nums[end]
            while prod >= k and st <= end:
                prod //= nums[st]
                st += 1
            ans += end - st + 1
        return ans


def test_num_subarray_product_less_than_k():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100) == 8
    print("OK")

    print("Test 2... ", end="")
    assert sol.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0) == 0
    print("OK")


if __name__ == "__main__":
    test_num_subarray_product_less_than_k()
