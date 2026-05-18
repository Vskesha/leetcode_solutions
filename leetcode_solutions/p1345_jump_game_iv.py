import unittest
from collections import defaultdict, deque
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        la = len(arr)

        if la < 3:
            return la - 1

        inds = defaultdict(list)
        for i, n in enumerate(arr):
            inds[n].append(i)

        seen_vals = set()
        distances = [-1] * la
        distances[0] = 0
        bfs = deque([0])

        while bfs:
            i = bfs.popleft()
            ndist = distances[i] + 1

            if i == la - 2:
                return ndist

            if (ni := i - 1) >= 0 and distances[ni] == -1:
                bfs.append(ni)
                distances[ni] = ndist

            if (ni := i + 1) < la and distances[ni] == -1:
                bfs.append(ni)
                distances[ni] = ndist

            if arr[i] in seen_vals:
                continue

            for ni in inds[arr[i]]:
                if ni == i or distances[ni] != -1:
                    continue
                if ni == la - 1:
                    return ndist
                bfs.append(ni)
                distances[ni] = ndist

            seen_vals.add(arr[i])

        return la - 1


class Solution2:
    def minJumps(self, arr: List[int]) -> int:
        la = len(arr)

        if la < 3:
            return la - 1

        inds = defaultdict(list)
        for i, n in enumerate(arr):
            inds[n].append(i)

        seen_vals = set()
        visited = [False] * la
        visited[0] = True

        bfs = deque([0])
        dist = 0

        while bfs:
            dist += 1
            for _ in range(len(bfs)):
                i = bfs.popleft()

                if i == la - 2:
                    return dist

                if i > 0 and not visited[i - 1]:
                    bfs.append(i - 1)
                    visited[i - 1] = True

                if i < la - 1 and not visited[i + 1]:
                    bfs.append(i + 1)
                    visited[i + 1] = True

                if arr[i] in seen_vals:
                    continue

                for ni in inds[arr[i]]:
                    if ni == i or visited[ni]:
                        continue
                    if ni == la - 1:
                        return dist
                    bfs.append(ni)
                    visited[ni] = True

                seen_vals.add(arr[i])

        return la - 1


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minJumps"] * 4,
            "kwargs": [
                dict(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]),
                dict(arr=[7]),
                dict(arr=[7, 6, 9, 6, 9, 6, 9, 7]),
                dict(
                    arr=[
                        -10,
                        -25,
                        58,
                        -67,
                        28,
                        86,
                        58,
                        -29,
                        -10,
                        -10,
                        45,
                        -80,
                        86,
                        35,
                        -10,
                        58,
                        -10,
                        -98,
                        -9,
                        -98,
                        -10,
                        -67,
                        -29,
                        -6,
                        74,
                        46,
                        -29,
                        -5,
                        58,
                        58,
                        -17,
                        28,
                        -4,
                        -67,
                        28,
                        -98,
                        -4,
                        86,
                        -29,
                        -92,
                        -67,
                        58,
                        -76,
                        -27,
                        -9,
                        58,
                        -92,
                        -42,
                        -27,
                        -41,
                        58,
                        -25,
                        74,
                        -98,
                        -92,
                        -10,
                        -67,
                        -6,
                        -17,
                        -5,
                        -29,
                        -17,
                        -4,
                        28,
                        -17,
                        -80,
                        35,
                        -9,
                        32,
                        -29,
                        -76,
                        46,
                        -29,
                        -5,
                        -27,
                        35,
                        74,
                        -92,
                        -4,
                        -98,
                        -9,
                        -10,
                        -4,
                        -27,
                        -92,
                        74,
                        -98,
                        -29,
                        -42,
                        -9,
                        45,
                        -10,
                        -98,
                        28,
                    ]
                ),
            ],
            "expected": [3, 0, 1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
