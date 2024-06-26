import unittest
from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[k] - (i > k), am) for i, am in enumerate(tickets))


class Solution1:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        kt = tickets[k]
        ans = kt

        for i in range(k):
            ans += min(kt, tickets[i])

        for i in range(k + 1, n):
            ans += min(kt - 1, tickets[i])

        return ans


class Solution2:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        que = deque(range(n))
        ans = 0
        while True:
            ans += 1
            nxt = que.popleft()
            tickets[nxt] -= 1
            if tickets[nxt]:
                que.append(nxt)
            elif nxt == k:
                return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_time_required_to_buy_1(self):
        print("Test timeRequiredToBuy 1... ", end="")
        self.assertEqual(self.sol.timeRequiredToBuy(tickets=[2, 3, 2], k=2), 6)
        print("OK")

    def test_time_required_to_buy_2(self):
        print("Test timeRequiredToBuy 2... ", end="")
        self.assertEqual(self.sol.timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0), 8)
        print("OK")


if __name__ == "__main__":
    unittest.main()
