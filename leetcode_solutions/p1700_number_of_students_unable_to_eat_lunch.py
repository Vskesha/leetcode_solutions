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


def test_count_students():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]) == 0
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1])
        == 3
    )
    print("OK")


if __name__ == "__main__":
    test_count_students()
