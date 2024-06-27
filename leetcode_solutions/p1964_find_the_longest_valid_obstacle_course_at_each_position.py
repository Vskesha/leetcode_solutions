import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans, dis = [], []
        for obstacle in obstacles:
            if not dis or obstacle >= dis[-1]:
                dis.append(obstacle)
                ans.append(len(dis))
            else:
                idx = bisect_right(dis, obstacle)
                dis[idx] = obstacle
                ans.append(idx + 1)
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_longest_obstacle_course_at_each_position_1(self):
        print("Test longestObstacleCourseAtEachPosition 1... ", end="")
        self.assertListEqual(
            self.sol.longestObstacleCourseAtEachPosition(obstacles=[1, 2, 3, 2]),
            [1, 2, 3, 3],
        )
        print("OK")

    def test_longest_obstacle_course_at_each_position_2(self):
        print("Test longestObstacleCourseAtEachPosition 2... ", end="")
        self.assertListEqual(
            self.sol.longestObstacleCourseAtEachPosition(obstacles=[2, 2, 1]),
            [1, 2, 1],
        )
        print("OK")

    def test_longest_obstacle_course_at_each_position_3(self):
        print("Test longestObstacleCourseAtEachPosition 3... ", end="")
        self.assertListEqual(
            self.sol.longestObstacleCourseAtEachPosition(obstacles=[3, 1, 5, 6, 4, 2]),
            [1, 1, 2, 3, 2, 2],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
