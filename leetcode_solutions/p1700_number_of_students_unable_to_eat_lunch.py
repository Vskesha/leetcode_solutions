import unittest
from collections import Counter, deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        students = deque(students)
        for sandwich in sandwiches:
            if cnt[sandwich] == 0:
                break
            while sandwich != students[0]:
                students.append(students.popleft())
            cnt[students.popleft()] -= 1

        return len(students)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_count_students_1(self):
        print("Test countStudents 1... ", end="")
        self.assertEqual(
            self.sol.countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]), 0
        )
        print("OK")

    def test_count_students_2(self):
        print("Test countStudents 2... ", end="")
        self.assertEqual(
            self.sol.countStudents(
                students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]
            ),
            3,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
