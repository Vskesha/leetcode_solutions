from collections import defaultdict
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        aux = defaultdict(list)
        know = {0, firstPerson}

        for person1, person2, time in meetings:
            i1 = i2 = -1
            for i, group in enumerate(aux[time]):
                if person1 in group:
                    i1 = i
                if person2 in group:
                    i2 = i

            if i1 == i2 == -1:
                aux[time].append({person1, person2})
            elif i1 == -1:
                aux[time][i2].add(person1)
            elif i2 == -1:
                aux[time][i1].add(person2)
            elif i1 != i2:
                aux[time][i1].update(aux[time].pop(i2))

        for time in sorted(aux.keys()):
            for group in aux[time]:
                if know & group:
                    know.update(group)

        return list(know)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findAllPeople(
        n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1
    ) == [0, 1, 2, 3, 5]
    print("OK")

    print("Test 2... ", end="")
    assert sol.findAllPeople(
        n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3
    ) == [0, 1, 3]
    print("OK")

    print("Test 3... ", end="")
    assert sol.findAllPeople(
        n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1
    ) == [0, 1, 2, 3, 4]
    print("OK")


if __name__ == "__main__":
    test()
