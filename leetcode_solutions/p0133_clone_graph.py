import unittest
from collections import deque
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)

                cur_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def adj_list_to_graph(adj: List[List[int]]) -> Optional[Node]:
        if not adj:
            return None
        nodes = [Node(i) for i in range(1, len(adj) + 1)]
        for i, neighbors in enumerate(adj):
            for neib in neighbors:
                nodes[i].neighbors.append(nodes[neib - 1])
        return nodes[0]

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["cloneGraph"] * 3,
            "kwargs": [
                dict(node=adj_list_to_graph([[2, 4], [1, 3], [2, 4], [1, 3]])),
                dict(node=adj_list_to_graph([[]])),
                dict(node=adj_list_to_graph([])),
            ],
            "expected": [
                adj_list_to_graph([[2, 4], [1, 3], [2, 4], [1, 3]]),
                adj_list_to_graph([[]]),
                adj_list_to_graph([]),
            ],
            "assert_methods": ["assertSameGraphs"] * 3,
        },
    ]

    def assertSameGraphs(self, actual: Optional[Node], expected: Optional[Node]):
        if actual and expected:
            seen = {actual.val}
            bfs = deque([(actual, expected)])
            while bfs:
                curr, exp = bfs.popleft()
                self.assertEqual(curr.val, exp.val)
                self.assertEqual(len(curr.neighbors), len(exp.neighbors))
                for n1, n2 in zip(
                    sorted(curr.neighbors, key=lambda x: x.val),
                    sorted(exp.neighbors, key=lambda x: x.val),
                ):
                    if n1.val not in seen:
                        seen.add(n1.val)
                        bfs.append((n1, n2))
        else:
            self.assertIsNone(actual)
            self.assertIsNone(expected)


if __name__ == "__main__":
    unittest.main()
