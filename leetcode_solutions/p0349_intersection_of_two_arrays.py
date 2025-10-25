from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


def test_intersection():
    sol = Solution()

    print("Test 1... ", end="")
    assert set(sol.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2])) == {2}
    print("OK")

    print("Test 2... ", end="")
    assert set(sol.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])) == {
        9,
        4,
    }
    print("OK")


if __name__ == "__main__":
    test_intersection()
