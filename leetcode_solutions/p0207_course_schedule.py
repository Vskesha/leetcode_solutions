from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological_sort

        income = [0] * numCourses
        graph = defaultdict(list)

        for after, before in prerequisites:
            income[after] += 1
            graph[before].append(after)

        st = [i for i, n in enumerate(income) if not n]

        while st:
            curr = st.pop()
            for neib in graph[curr]:
                income[neib] -= 1
                if not income[neib]:
                    st.append(neib)

        return not any(income)


class Solution1:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for second, first in prerequisites:
            graph[first].append(second)
            indegrees[second] += 1

        zero_indegrees = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                zero_indegrees.append(i)

        counter = 0
        while zero_indegrees:
            curr_course = zero_indegrees.popleft()
            counter += 1
            for next_course in graph[curr_course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    zero_indegrees.append(next_course)

        return counter == numCourses


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        for second, first in prerequisites:
            graph[first].append(second)

        nodes_which_not_lead_to_cycle = set()

        def leads_to_cycle(node: int, track: set) -> bool:
            if node in nodes_which_not_lead_to_cycle:
                return False
            for neib in graph[node]:
                if neib in track:
                    return True
                track.add(neib)
                if leads_to_cycle(neib, track):
                    return True
                track.remove(neib)
            nodes_which_not_lead_to_cycle.add(node)
            return False

        for node in range(numCourses):
            if leads_to_cycle(node, {node}):
                return False

        return True


def main():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.canFinish(numCourses=2, prerequisites=[[1, 0]]) is True
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]) is False
    print('OK')


if __name__ == '__main__':
    main()
