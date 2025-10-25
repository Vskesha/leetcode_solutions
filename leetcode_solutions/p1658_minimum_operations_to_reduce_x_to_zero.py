from collections import deque
from typing import List


# simple greedy two pointer solution
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ln = len(nums)
        ts = sum(nums)

        if ts < x:
            return -1
        if ts == x:
            return ln

        l = 0
        ans = ln
        for r in range(ln):
            ts -= nums[r]
            while ts < x:
                ts += nums[l]
                l += 1
            if ts == x:
                ans = min(ans, l + ln - r - 1)

        return -1 if ans == ln else ans


# too much complicated :)
class Solution2:
    def minOperations(self, nums: List[int], x: int) -> int:
        sn = sum(nums)
        ln = len(nums)
        if sn < x:
            return -1
        if sn == x:
            return ln

        bfs = deque()
        bfs.append((0, 0, 0))
        while bfs:
            op, left, total = bfs.popleft()
            if total == x:
                return op
            op += 1
            if left == 0:
                new_total = total + nums[-op]
                if new_total <= x:
                    bfs.append((op, left, new_total))
            new_total = total + nums[left]
            if new_total <= x:
                bfs.append((op, left + 1, new_total))
        return -1


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.minOperations(nums=[1, 1, 4, 2, 3], x=5) == 2
    print("ok\nTest 2 ... ", end="")
    assert sol.minOperations(nums=[5, 6, 7, 8, 9], x=4) == -1
    print("ok\nTest 3 ... ", end="")
    assert sol.minOperations(nums=[3, 2, 20, 1, 1, 3], x=10) == 5
    print("ok")


if __name__ == "__main__":
    test()
