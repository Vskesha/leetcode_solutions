from math import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ln1, ln2 = len(nums1), len(nums2)
        tl = ln1 + ln2
        hf = (tl + 1) // 2

        l, r = 0, ln1
        while l <= r:
            i1 = (l + r) // 2
            i2 = hf - i1
            a = nums1[i1 - 1] if i1 else -inf
            b = nums1[i1] if i1 < ln1 else inf
            c = nums2[i2 - 1] if i2 else -inf
            d = nums2[i2] if i2 < ln2 else inf
            if a > d:
                r = i1 - 1
            elif b < c:
                l = i1 + 1
            elif tl % 2:
                return float(max(a, c))
            else:
                return (max(a, c) + min(b, d)) / 2


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        l1, l2 = len(nums1), len(nums2)
        middle_odd = (l1 + l2) % 2
        middle = (l1 + l2 - 1) // 2
        nums1.append(10 ** 8)
        nums2.append(10 ** 8)
        for _ in range(middle):
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        res = sorted(nums1[i:i + 2] + nums2[j:j + 2])
        return float(res[0]) if middle_odd else (res[0] + res[1]) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ln1, ln2 = len(nums1), len(nums2)
        tl = ln1 + ln2
        hf = (tl - 1) // 2

        if ln1 == ln2 == 1:
            return (nums1[0] + nums2[0]) / 2

        i2 = hf - ln1
        if not nums1 or (i2 >= 0 and nums2[i2] >= nums1[-1]):
            return float(nums2[i2]) if tl % 2 else (nums2[i2] + nums2[i2 + 1]) / 2

        if nums1[0] >= nums2[hf - 1]:
            ans = sorted(nums1[:2] + nums2[hf:hf + 2])
            return float(ans[0]) if tl % 2 else sum(ans[:2]) / 2

        i1, l, r = 1, 1, ln1 - 1

        while l < r:
            i1 = (l + r) // 2
            i2 = hf - i1
            if nums2[i2 - 1] >= nums1[i1]:
                l = i1 + 1
            elif nums1[i1 - 1] >= nums2[i2]:
                r = i1
            else:
                l = i1
                break

        i2 = hf - l
        ans = sorted(nums1[l:l + 2] + nums2[i2:i2 + 2])
        return float(ans[0]) if tl % 2 else sum(ans[:2]) / 2


class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ln1, ln2 = len(nums1), len(nums2)
        tl = ln1 + ln2
        hf = (tl + 1) // 2

        l, r = 0, ln1
        while l <= r:
            i1 = (l + r) // 2
            i2 = hf - i1
            if i1 and i2 < ln2 and nums1[i1 - 1] > nums2[i2]:
                r = i1 - 1
            elif i2 and i1 < ln1 and nums2[i2 - 1] > nums1[i1]:
                l = i1 + 1
            elif tl % 2:
                ans = -inf
                if i1:
                    ans = max(ans, nums1[i1 - 1])
                if i2:
                    ans = max(ans, nums2[i2 - 1])
                return float(ans)
            else:
                ans = -inf
                if i1:
                    ans = max(ans, nums1[i1 - 1])
                if i2:
                    ans = max(ans, nums2[i2 - 1])
                ans2 = inf
                if i1 < ln1:
                    ans2 = min(ans2, nums1[i1])
                if i2 < ln2:
                    ans2 = min(ans2, nums2[i2])
                return (ans + ans2) / 2


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2.0
    print('OK')

    print('Test 2... ', end='')
    assert sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.5
    print('ok')

    print('Test 3... ', end='')
    assert sol.findMedianSortedArrays(nums1=[100000], nums2=[100001]) == 100000.5
    print('OK')

    print('Test 4... ', end='')
    assert sol.findMedianSortedArrays(nums1=[1, 2, 3], nums2=[4, 5, 6]) == 3.5
    print('OK')

    print('Test 5... ', end='')
    assert sol.findMedianSortedArrays(nums1=[1, 2, 2], nums2=[1, 2, 3]) == 2.0
    print('OK')

    print('Test 6... ', end='')
    assert sol.findMedianSortedArrays(nums1=[], nums2=[1, 2, 3, 4]) == 2.5
    print('OK')


if __name__ == '__main__':
    test()
