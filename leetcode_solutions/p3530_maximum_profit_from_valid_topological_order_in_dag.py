import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxProfit(
        self, n: int, edges: List[List[int]], score: List[int]
    ) -> int:
        is_root = {i: True for i in range(n)}
        for u, v in edges:
            is_root[v] = False
        # root = [i for i, ir in is_root.items() if ir][0]
        # print(root)

        children = {i: [] for i in range(n)}
        for u, v in edges:
            children[u].append(v)
        # print(children)

        parents = {i: [] for i in range(n)}
        for u, v in edges:
            parents[v].append(u)

        roots_a = set()
        roots_b = set()
        for i in range(n):
            if is_root[i]:
                if len(children[i]) == 0:
                    roots_b.add(i)
                else:
                    roots_a.add(i)

        FUTURE_SCORE = {}

        def get_best_score(s, i, options_a, options_b, visited):
            if frozenset(visited) in FUTURE_SCORE:
                return s + FUTURE_SCORE[frozenset(visited)]

            # print(s, i, options_a, options_b)
            if len(options_b) > 0:
                e0 = min(options_b, key=lambda i: score[i])
                options_b.remove(e0)
                visited.add(e0)
                new_score = get_best_score(
                    s + i * score[e0], i + 1, options_a, options_b, visited
                )
                visited.remove(e0)
                options_b.add(e0)
            else:
                new_score = s

            for e in list(options_a):
                options_a.remove(e)
                visited.add(e)
                for c in children[e]:
                    if any(p not in visited for p in parents[c]):
                        continue
                    if len(children[c]) == 0:
                        options_b.add(c)
                    else:
                        options_a.add(c)

                e_score = get_best_score(
                    s + i * score[e], i + 1, options_a, options_b, visited
                )

                for c in children[e]:
                    if any(p not in visited for p in parents[c]):
                        continue
                    if len(children[c]) == 0:
                        options_b.remove(c)
                    else:
                        options_a.remove(c)
                visited.remove(e)
                options_a.add(e)

                new_score = max(new_score, e_score)
            # print(s, i, options_a, options_b, "->", new_score)
            FUTURE_SCORE[frozenset(visited)] = new_score - s
            return new_score

        # return get_best_score(0, 1, {root}, set())
        return get_best_score(0, 1, roots_a, roots_b, set())


class Solution2:
    def maxProfit(
        self, n: int, edges: List[List[int]], score: List[int]
    ) -> int:
        need = [0] * n
        for i, j in edges:
            need[j] |= 1 << i
        dp = [-1] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            pos = mask.bit_count() + 1
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    if (mask & need[i]) == need[i]:
                        mask2 = mask | (1 << i)
                        dp[mask2] = max(dp[mask2], dp[mask] + score[i] * pos)
        return dp[(1 << n) - 1]


class Solution3:
    def maxProfit(
        self, n: int, edges: List[List[int]], score: List[int]
    ) -> int:
        income = [0] * n
        adj = [[] for _ in range(n)]
        for fr, to in edges:
            adj[fr].append(to)
            income[to] += 1

        def get_max_score(income, pos):
            if pos > n:
                return 0

            ans = 0
            for curr in range(n):
                if income[curr]:
                    continue
                income[curr] -= 1
                for neib in adj[curr]:
                    income[neib] -= 1
                sc = score[curr] * pos
                sc += get_max_score(income, pos + 1)
                if sc > ans:
                    ans = sc
                income[curr] += 1
                for neib in adj[curr]:
                    income[neib] += 1

            return ans

        return get_max_score(income, 1)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxProfit"] * 2,
            "kwargs": [
                dict(n=2, edges=[[0, 1]], score=[2, 3]),
                dict(n=3, edges=[[0, 1], [0, 2]], score=[1, 6, 3]),
            ],
            "expected": [8, 25],
        },
    ]


if __name__ == "__main__":
    unittest.main()
