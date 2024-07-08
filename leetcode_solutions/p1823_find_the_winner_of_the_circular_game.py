import unittest
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1


class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        def dp(n: int, k: int) -> int:
            if n == 1:
                return 0
            return (dp(n - 1, k) + k) % n

        return dp(n, k) + 1


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        dummy = curr = Node()
        for val in range(1, n + 1):
            curr.next = Node(val)
            curr = curr.next
        curr.next = dummy.next
        k -= 1
        while curr != curr.next:
            for _ in range(k):
                curr = curr.next
            curr.next = curr.next.next

        return curr.val


class Solution3:
    def findTheWinner(self, n: int, k: int) -> int:
        que = deque(range(1, n + 1))
        k -= 1
        ans = 0

        while que:
            for i in range(k):
                que.append(que.popleft())
            ans = que.popleft()

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_find_the_winner_1(self):
        print("Test findTheWinner 1... ", end="")
        self.assertEqual(self.sol.findTheWinner(n=5, k=2), 3)
        print("OK")

    def test_find_the_winner_2(self):
        print("Test findTheWinner 2... ", end="")
        self.assertEqual(self.sol.findTheWinner(n=6, k=5), 1)
        print("OK")


if __name__ == "__main__":
    unittest.main()
