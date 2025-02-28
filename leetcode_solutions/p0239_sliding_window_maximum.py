from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()

        for i in range(k):
            val = nums[i]
            while dq and nums[dq[-1]] <= val:
                dq.pop()
            dq.append(i)

        res = [nums[dq[0]]]

        for i in range(k, len(nums)):
            if dq[0] == i - k:
                dq.popleft()
            val = nums[i]
            while dq and nums[dq[-1]] <= val:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])

        return res


def main():
    sol = Solution()
    print(' [3, 3, 5, 5, 6, 7]\n', sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(' [1]\n', sol.maxSlidingWindow(nums=[1], k=1))


if __name__ == '__main__':
    main()
