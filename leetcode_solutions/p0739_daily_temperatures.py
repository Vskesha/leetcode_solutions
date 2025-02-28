import unittest
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lt = len(temperatures)
        st, ans = [], [0] * lt
        for i, t in enumerate(temperatures):
            while st and st[-1][0] < t:
                _, pi = st.pop()
                ans[pi] = i - pi
            st.append((t, i))
        return ans


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lt = len(temperatures)
        ans = [0] * lt
        st = []
        for i in range(lt - 1, -1, -1):
            t = temperatures[i]
            while st and st[-1][0] <= t:
                st.pop()
            if st:
                ans[i] = st[-1][1] - i
            st.append((t, i))
        return ans


class Solution3:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        lt = len(temperatures)
        ans = [0] * lt

        for i in range(lt - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_dailyTemperatures_1(self):
        print("Test dailyTemperatures 1... ", end="")
        self.assertListEqual(
            [1, 1, 4, 2, 1, 1, 0, 0],
            self.sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]),
        )
        print("OK")

    def test_dailyTemperatures_2(self):
        print("Test dailyTemperatures 2... ", end="")
        self.assertListEqual(
            [1, 1, 1, 0],
            self.sol.dailyTemperatures(temperatures=[30, 40, 50, 60]),
        )
        print("OK")

    def test_dailyTemperatures_3(self):
        print("Test dailyTemperatures 3... ", end="")
        self.assertListEqual(
            [1, 1, 0],
            self.sol.dailyTemperatures(temperatures=[30, 60, 90]),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
