from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            if height[l] < height[r]:
                ans = max(ans, height[l] * (r - l))
                l += 1
            else:
                ans = max(ans, height[r] * (r - l))
                r -= 1

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert sol.maxArea(height) == 49
    print('OK')

    print('Test 2... ', end='')
    height = [1, 1]
    assert sol.maxArea(height) == 1
    print('OK')

    print('Test 3... ', end='')
    height = [4, 3, 2, 1]
    assert sol.maxArea(height) == 4
    print('OK')


if __name__ == '__main__':
    test()
