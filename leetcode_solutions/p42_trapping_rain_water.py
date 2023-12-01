from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left, right = height[0], height[-1]
        ans = 0
        while l < r:
            if left < right:
                l += 1
                if height[l] < left:
                    ans += left - height[l]
                else:
                    left = height[l]
            else:
                r -= 1
                if height[r] < right:
                    ans += right - height[r]
                else:
                    right = height[r]

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    print('OK')

    print('Test 2... ', end='')
    assert sol.trap(height=[4, 2, 0, 3, 2, 5]) == 9
    print('OK')


if __name__ == '__main__':
    test()
