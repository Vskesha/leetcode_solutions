from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        l1, l2 = len(nums1), len(nums2)
        middle_odd = (l1 + l2) % 2
        middle = (l1 + l2 - 1) // 2
        nums1.append(10**8)
        nums2.append(10**8)
        for _ in range(middle):
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        res = sorted(nums1[i:i+2] + nums2[j:j+2])
        return float(res[0]) if middle_odd else (res[0] + res[1]) / 2


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2.0
    print('ok\nTest 2 ... ', end='')
    assert sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.5
    print('ok')


if __name__ == '__main__':
    test()