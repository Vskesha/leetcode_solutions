import unittest
from typing import List


class Solution:
    def largestRectangleArea(self, bars: List[int]) -> int:
        st, res = [], 0
        bars.append(-1)
        for bar in bars:
            step = 0
            while st and st[-1][1] >= bar:
                w, h = st.pop()
                step += w
                res = max(res, step * h)
            st.append((step + 1, bar))
        return res


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans = [], 0
        heights.append(-1)

        for i, h in enumerate(heights):
            pi = i
            while stack and stack[-1][1] > h:
                pi, ph = stack.pop()
                ans = max(ans, ph * (i - pi))
            stack.append((pi, h))

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_largest_rectangle_area_1(self):
        print("Test largestRectangleArea 1... ", end="")
        self.assertEqual(self.sol.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        print("OK")

    def test_largest_rectangle_area_2(self):
        print("Test largestRectangleArea 2... ", end="")
        self.assertEqual(self.sol.largestRectangleArea([2, 4]), 4)
        print("OK")


if __name__ == "__main__":
    unittest.main()
