from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        li, ri = 0, len(height) - 1
        left, right = height[li], height[ri]
        res = 0

        while li < ri:
            if left < right:
                li += 1
                left = max(left, height[li])
                res += left - height[li]
            else:
                ri -= 1
                right = max(right, height[ri])
                res += right - height[ri]

        return res


class Solution1:
    def trap(self, height: List[int]) -> int:
        li, ri = 0, len(height) - 1
        left, right = height[li], height[ri]
        res = 0

        while li < ri:
            if left < right:
                li += 1
                new_left = height[li]
                if new_left > left:
                    left = new_left
                else:
                    res += left - new_left
            else:
                ri -= 1
                new_right = height[ri]
                if new_right > right:
                    right = new_right
                else:
                    res += right - new_right

        return res


class Solution2:
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

    print("Test 1... ", end="")
    assert sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.trap(height=[4, 2, 0, 3, 2, 5]) == 9
    print("OK")


if __name__ == "__main__":
    test()
