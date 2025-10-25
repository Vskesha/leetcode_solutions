from heapq import _heapify_max, _heappop_max, heapify, heappop, heappushpop


class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapify(heap)
        for i in range(k, len(nums)):
            heappushpop(heap, nums[i])
        return heap[0]


class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        ns = [-n for n in nums]
        heapify(ns)
        for _ in range(1, k):
            heappop(ns)
        return -heappop(ns)


class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        _heapify_max(nums)
        for _ in range(1, k):
            _heappop_max(nums)
        return nums[0]


def main():
    sol = Solution()
    print("5 ===", sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    print("4 ===", sol.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))


if __name__ == "__main__":
    main()
