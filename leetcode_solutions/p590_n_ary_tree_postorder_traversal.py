import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return f"Node({self.val}, {[ch.val for ch in self.children]})"


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        ans = []
        for child in root.children:
            ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def arr_to_n_ary_tree(arr: List[int]) -> Node:
        if not arr:
            return None

        root = Node(arr[0], [])
        queue = deque([root])
        i, la = 2, len(arr)

        while queue:
            node = queue.popleft()
            while i < la and arr[i] is not None:
                child = Node(arr[i], [])
                node.children.append(child)
                queue.append(child)
                i += 1
            i += 1

        return root

    null = None
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["postorder"] * 2,
            "kwargs": [
                dict(root=arr_to_n_ary_tree([1, null, 3, 2, 4, null, 5, 6])),
                dict(
                    root=arr_to_n_ary_tree(
                        [
                            1,
                            null,
                            2,
                            3,
                            4,
                            5,
                            null,
                            null,
                            6,
                            7,
                            null,
                            8,
                            null,
                            9,
                            10,
                            null,
                            null,
                            11,
                            null,
                            12,
                            null,
                            13,
                            null,
                            null,
                            14,
                        ]
                    )
                ),
            ],
            "expected": [
                [5, 6, 3, 2, 4, 1],
                [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
