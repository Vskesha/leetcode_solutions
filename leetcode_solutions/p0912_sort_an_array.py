import unittest
from heapq import heapify, heappop
from math import inf
from random import randint
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        m = min(nums)
        aux = [0] * (max(nums) - m + 1)
        for n in nums:
            aux[n - m] += 1

        ans = []
        for i, q in enumerate(aux):
            for _ in range(q):
                ans.append(i + m)

        return ans


class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        return [heappop(nums) for _ in range(len(nums))]


class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums: List[int], li: int, ri: int) -> int:
        pivot = nums[(li + ri) // 2]
        while True:
            while nums[li] < pivot:
                li += 1
            while nums[ri] > pivot:
                ri -= 1
            if li >= ri:
                return ri
            nums[li], nums[ri] = nums[ri], nums[li]
            li += 1
            ri -= 1

    def sort(self, nums: List[int], li: int, ri: int) -> None:
        if li < ri:
            pi = self.partition(nums, li, ri)
            self.sort(nums, li, pi)
            self.sort(nums, pi + 1, ri)


class Solution3:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(i: int, j: int, nums: List[int]) -> None:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]

        def partition(li: int, ri: int, nums: List[int]) -> tuple[int, int]:
            randi = randint(li, ri)
            swap(ri, randi, nums)
            pivot = nums[ri]
            lpi = rpi = li
            for i in range(li, ri):
                if nums[i] == pivot:
                    swap(i, rpi, nums)
                    rpi += 1
                elif nums[i] < pivot:
                    swap(i, rpi, nums)
                    swap(lpi, rpi, nums)
                    lpi += 1
                    rpi += 1
            swap(rpi, ri, nums)
            rpi += 1
            return lpi, rpi

        def sort(li: int, ri: int, nums: List[int]) -> None:
            if li < ri:
                lpi, rpi = partition(li, ri, nums)
                sort(li, lpi - 1, nums)
                sort(rpi, ri, nums)

        sort(0, len(nums) - 1, nums)
        return nums


class Solution4:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(0, len(nums) - 1, nums)
        return nums

    def swap(self, i: int, j: int, nums: List[int]) -> None:
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]

    def partition(self, li: int, ri: int, nums: List[int]) -> tuple[int, int]:
        randi = randint(li, ri)
        self.swap(ri, randi, nums)
        pivot = nums[ri]
        lpi = rpi = li
        for i in range(li, ri):
            if nums[i] == pivot:
                self.swap(i, rpi, nums)
                rpi += 1
            elif nums[i] < pivot:
                self.swap(i, rpi, nums)
                self.swap(lpi, rpi, nums)
                lpi += 1
                rpi += 1
        self.swap(rpi, ri, nums)
        rpi += 1
        return lpi, rpi

    def sort(self, li: int, ri: int, nums: List[int]) -> None:
        if li < ri:
            lpi, rpi = self.partition(li, ri, nums)
            self.sort(li, lpi - 1, nums)
            self.sort(rpi, ri, nums)


class Solution5:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        nums1 = self.sortArray(nums[:mid])
        nums2 = self.sortArray(nums[mid:])

        i = j = k = 0
        l1, l2 = len(nums1), len(nums2)
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1

        while i < l1:
            nums[k] = nums1[i]
            i += 1
            k += 1

        while j < l2:
            nums[k] = nums2[j]
            j += 1
            k += 1

        return nums


class Solution6:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        nums1 = self.sortArray(nums[:mid])
        nums2 = self.sortArray(nums[mid:])
        if nums1[-1] < nums2[-1]:
            nums1, nums2 = iter(nums2), iter(nums1)
        else:
            nums1, nums2 = iter(nums1), iter(nums2)
        n2, k = next(nums2, inf), 0

        for n1 in nums1:
            while n2 <= n1:
                nums[k] = n2
                k += 1
                n2 = next(nums2, inf)
            nums[k] = n1
            k += 1

        return nums


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sortArray_1(self):
        print("Test sortArray 1... ", end="")
        self.assertListEqual(
            [1, 2, 3, 5], self.sol.sortArray(nums=[5, 2, 3, 1])
        )
        print("OK")

    def test_sortArray_2(self):
        print("Test sortArray 2... ", end="")
        self.assertListEqual(
            [0, 0, 1, 1, 2, 5], self.sol.sortArray(nums=[5, 1, 1, 2, 0, 0])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
