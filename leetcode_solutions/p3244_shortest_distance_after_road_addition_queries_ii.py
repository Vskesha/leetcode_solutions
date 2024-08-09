import unittest
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        ans = []
        jump = list(range(1, n))
        n -= 1
        for u, v in queries:
            while jump[u] < v:
                jump[u], u = v, jump[u]
                n -= 1
            ans.append(n)
        return ans


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


class Solution2:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        head = None
        avail = {}
        for i in range(n - 1, -1, -1):
            head = ListNode(i, head)
            avail[i] = head

        n -= 1
        ans = []
        for fr, to in queries:
            if fr in avail:
                st = avail[fr]
                curr = st.next
                while curr.val < to:
                    n -= 1
                    del avail[curr.val]
                    curr = curr.next
                st.next = curr
            ans.append(n)

        return ans


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        head = None
        nodes = {}
        for i in range(n - 1, -1, -1):
            head = ListNode(i, head)
            nodes[i] = head

        n -= 1
        ans = []
        for fr, to in queries:
            curr, end = nodes[fr], nodes[to]
            while curr.next.val < to:
                curr.next, curr = end, curr.next
                n -= 1
            ans.append(n)

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol = Solution()

    def test_shortestDistanceAfterQueries_1(self):
        print("Test shortestDistanceAfterQueries 1... ", end="")
        self.assertEqual(
            self.sol.shortestDistanceAfterQueries(
                n=5, queries=[[2, 4], [0, 2], [0, 4]]
            ),
            [3, 2, 1],
        )
        print("OK")

    def test_shortestDistanceAfterQueries_2(self):
        print("Test shortestDistanceAfterQueries 2... ", end="")
        self.assertEqual(
            self.sol.shortestDistanceAfterQueries(n=4, queries=[[0, 3], [0, 2]]), [1, 1]
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
