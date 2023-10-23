from collections import deque
from heapq import heappop, heappush
from sortedcontainers import SortedList
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        for i in range(1, len(nums)):
            while q and nums[q[-1]] <= nums[i - 1]:
                q.pop()
            q.append(i - 1)
            while q[0] < i - k:
                q.popleft()
            if nums[q[0]] > 0:
                nums[i] += nums[q[0]]

        return max(nums)


class SolutionB:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(1, len(nums)):
            heappush(heap, (-nums[i - 1], i - 1))
            while heap[0][1] < i - k:
                heappop(heap)
            if heap[0][0] < 0:
                nums[i] -= heap[0][0]

        return max(nums)


class Solution1:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if queue and i - queue[0] > k:
                queue.popleft()

            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()

            if dp[i] > 0:
                queue.append(i)

        return max(dp)


class Solution2:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        window = SortedList([0])
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i - k])

        return max(dp)


class Solution3:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heappop(heap)

            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heappush(heap, (-curr, i))

        return ans


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.constrainedSubsetSum(nums=[10, 2, -10, 5, 20], k=2) == 37
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.constrainedSubsetSum(nums=[-1, -2, -3], k=1) == -1
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2) == 23
    print('ok')


if __name__ == '__main__':
    test()
