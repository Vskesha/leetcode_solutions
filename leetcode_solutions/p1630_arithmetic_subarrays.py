from heapq import heapify, heappop
from itertools import pairwise
from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], left: List[int], right: List[int]
    ) -> List[bool]:

        def is_arithmetic(li, ri):
            if ri - li < 3:
                return True
            ns = nums[li:ri]
            heapify(ns)
            prev = heappop(ns)
            curr = heappop(ns)
            d = curr - prev
            while ns:
                prev = curr
                curr = heappop(ns)
                if curr - prev != d:
                    return False
            return True

        return [is_arithmetic(left[i], right[i] + 1) for i in range(len(left))]


class Solution1:
    def checkArithmeticSubarrays(
        self, nums: List[int], left: List[int], right: List[int]
    ) -> List[bool]:

        def is_arithmetic(nums):
            if len(nums) == 1:
                return True
            heapify(nums)
            prev = heappop(nums)
            curr = heappop(nums)
            d = curr - prev
            while nums:
                prev = curr
                curr = heappop(nums)
                if curr - prev != d:
                    return False
            return True

        return [
            is_arithmetic(nums[left[i] : right[i] + 1])
            for i in range(len(left))
        ]


class Solution2:
    def checkArithmeticSubarrays(
        self, nums: List[int], left: List[int], right: List[int]
    ) -> List[bool]:
        ans = []
        for li, ri in zip(left, right):
            if ri - li < 2:
                ans.append(True)
                continue
            ns = nums[li : ri + 1]
            heapify(ns)
            prev, curr = heappop(ns), heappop(ns)
            d = curr - prev
            while ns:
                prev, curr = curr, heappop(ns)
                if curr - prev != d:
                    ans.append(False)
                    break
            else:
                ans.append(True)

        return ans


class Solution3:
    def checkArithmeticSubarrays(
        self, nums: List[int], left: List[int], right: List[int]
    ) -> List[bool]:
        ans = []
        for li, ri in zip(left, right):
            if ri - li < 2:
                ans.append(True)
                continue
            ns = sorted(nums[li : ri + 1])
            d = ns[1] - ns[0]
            for p, n in pairwise(ns):
                if n - p != d:
                    ans.append(False)
                    break
            else:
                ans.append(True)

        return ans


class Solution4:
    def checkArithmeticSubarrays(
        self, nums: List[int], left: List[int], right: List[int]
    ) -> List[bool]:
        ans = []
        for li, ri in zip(left, right):
            if ri - li < 2:
                ans.append(True)
                continue
            ns = sorted(nums[li : ri + 1])
            d = ns[1] - ns[0]
            for i in range(2, len(ns)):
                if ns[i] - ns[i - 1] != d:
                    ans.append(False)
                    break
            else:
                ans.append(True)

        return ans


def test():
    sol = Solution()
    true = True
    false = False

    print("Test 1 ... ", end="")
    assert sol.checkArithmeticSubarrays(
        nums=[4, 6, 5, 9, 3, 7], left=[0, 0, 2], right=[2, 3, 5]
    ) == [true, false, true]
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.checkArithmeticSubarrays(
        nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
        left=[0, 1, 6, 4, 8, 7],
        right=[4, 4, 9, 7, 9, 10],
    ) == [false, true, false, false, true, true]
    print("OK")


if __name__ == "__main__":
    test()
