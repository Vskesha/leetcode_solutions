from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        income = [0] * numCourses
        graph = defaultdict(list)

        for after, before in prerequisites:
            income[after] += 1
            graph[before].append(after)

        st = [i for i, n in enumerate(income) if not n]
        i = 0

        while i < len(st):
            curr = st[i]
            for neib in graph[curr]:
                income[neib] -= 1
                if not income[neib]:
                    st.append(neib)
            i += 1

        return st if len(st) == numCourses else []


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    print('OK')

    print('Test 2... ', end='')
    assert sol.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    print('OK')

    print('Test 3... ', end='')
    assert sol.findOrder(numCourses=1, prerequisites=[]) == [0]
    print('OK')


if __name__ == '__main__':
    test()
