import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        lt = len(tasks)
        lw = len(workers)
        tasks.sort()
        workers.sort()

        def can_complete(tn: int, p: int) -> bool:
            tq = deque()
            ti = 0

            for wi in range(lw - tn, lw):
                w = workers[wi]
                if not tq:
                    tq.append(tasks[ti])
                    ti += 1
                if w < tq[0]:
                    if not p or w + strength < tq[0]:
                        return False
                    while ti < tn and tasks[ti] <= w + strength:
                        tq.append(tasks[ti])
                        ti += 1
                    tq.pop()
                    p -= 1
                else:
                    tq.popleft()

            return True

        left, right = 0, min(lt, lw)
        while left < right:
            mid = (left + right + 1) // 2
            if can_complete(mid, pills):
                left = mid
            else:
                right = mid - 1
        return right


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxTaskAssign"] * 4,
            "kwargs": [
                dict(tasks=[3, 2, 1], workers=[0, 3, 3], pills=1, strength=1),
                dict(tasks=[5, 4], workers=[0, 0, 0], pills=1, strength=5),
                dict(
                    tasks=[5, 9, 8, 5, 9], workers=[1, 6, 4, 2, 6], pills=1, strength=5
                ),
                dict(
                    tasks=[10, 15, 30],
                    workers=[0, 10, 10, 10, 10],
                    pills=3,
                    strength=10,
                ),
            ],
            "expected": [3, 1, 3, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
