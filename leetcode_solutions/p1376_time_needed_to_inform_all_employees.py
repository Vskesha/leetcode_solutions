import unittest
from collections import defaultdict, deque
from typing import List


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        emps = defaultdict(list)
        for i, m in enumerate(manager):
            emps[m].append(i)

        queue = deque([(headID)])
        while queue:
            emp = queue.popleft()
            for sub in emps[emp]:
                informTime[sub] += informTime[emp]
                queue.append(sub)

        return max(informTime)


class Solution2:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        subordinates = [[] for _ in range(n + 1)]
        for ID, boss in enumerate(manager):
            subordinates[boss].append(ID)

        def time_needed(boss):
            if not subordinates[boss]:
                return 0
            ans = informTime[boss]
            ans += max(
                time_needed(subordinate) for subordinate in subordinates[boss]
            )

            return ans

        return time_needed(headID)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_num_of_minutes_1(self):
        print("Test numOfMinutes 1... ", end="")
        self.assertEqual(
            self.sol.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]),
            0,
        )
        print("OK")

    def test_num_of_minutes_2(self):
        print("Test numOfMinutes 2... ", end="")
        self.assertEqual(
            self.sol.numOfMinutes(
                n=6,
                headID=2,
                manager=[2, 2, -1, 2, 2, 2],
                informTime=[0, 0, 1, 0, 0, 0],
            ),
            1,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
