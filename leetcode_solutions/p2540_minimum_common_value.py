from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        i = j = 0
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return -1


class Solution2:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = iter(nums1), iter(nums2)
        v1, v2 = next(n1, None), next(n2, None)
        while v1 and v2:
            if v1 == v2:
                return v1
            elif v1 > v2:
                v2 = next(n2, None)
            else:
                v1 = next(n1, None)
        return -1


def test_get_common():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.getCommon(nums1=[1, 2, 3], nums2=[2, 4]) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]) == 2
    print("OK")


if __name__ == "__main__":
    test_get_common()
