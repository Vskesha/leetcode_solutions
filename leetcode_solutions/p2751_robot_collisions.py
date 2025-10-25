import unittest
from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        stack, ans, idx = [], [], range(len(positions))
        for _, h, d, i in sorted(zip(positions, healths, directions, idx)):
            if d == "R":
                stack.append((i, h))
                continue
            while stack:
                li, lh = stack.pop()
                if lh < h:
                    h -= 1
                    continue
                if lh > h:
                    stack.append((li, lh - 1))
                h = 0
                break
            if not stack and h:
                ans.append((i, h))
        return [h for _, h in sorted(ans + stack)]


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_survived_robots_healths_1(self):
        print("Test survivedRobotsHealths 1... ", end="")
        self.assertEqual(
            self.sol.survivedRobotsHealths(
                positions=[5, 4, 3, 2, 1],
                healths=[2, 17, 9, 15, 10],
                directions="RRRRR",
            ),
            [2, 17, 9, 15, 10],
        )
        print("OK")

    def test_survived_robots_healths_2(self):
        print("Test survivedRobotsHealths 2... ", end="")
        self.assertEqual(
            self.sol.survivedRobotsHealths(
                positions=[3, 5, 2, 6],
                healths=[10, 10, 15, 12],
                directions="RLRL",
            ),
            [14],
        )
        print("OK")

    def test_survived_robots_healths_3(self):
        print("Test survivedRobotsHealths 3... ", end="")
        self.assertEqual(
            self.sol.survivedRobotsHealths(
                positions=[1, 2, 5, 6],
                healths=[10, 10, 11, 11],
                directions="RLRL",
            ),
            [],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
