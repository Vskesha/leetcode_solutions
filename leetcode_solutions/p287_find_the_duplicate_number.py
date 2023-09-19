from typing import List


# Floyd's method to find a cycle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[nums[0]]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return n
            nums_set.add(n)


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        mask = 0
        for n in nums:
            if mask & 1 << n:
                return n
            mask |= 1 << n


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.findDuplicate(nums=[1, 3, 4, 2, 2]) == 2
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.findDuplicate(nums=[3, 1, 3, 4, 2]) == 3
    print('ok')


if __name__ == '__main__':
    test()
