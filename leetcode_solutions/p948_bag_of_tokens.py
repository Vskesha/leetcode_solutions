from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or tokens[0] > power:
            return 0
        l, r = 0, len(tokens) - 1
        while True:
            while l <= r and power >= tokens[l]:
                power -= tokens[l]
                l += 1
            if l < r:
                power += tokens[r]
                r -= 1
            else:
                return l + r + 1 - len(tokens)


class Solution2:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or tokens[0] > power:
            return 0
        l, r = 0, len(tokens) - 1
        ans = 0
        while True:
            while l <= r and power >= tokens[l]:
                ans += 1
                power -= tokens[l]
                l += 1
            if l < r:
                ans -= 1
                power += tokens[r]
                r -= 1
            else:
                return ans


def test_bag_of_tokens_score():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.bagOfTokensScore(tokens=[100], power=50) == 0
    print("OK")

    print("Test 2... ", end="")
    assert sol.bagOfTokensScore(tokens=[200, 100], power=150) == 1
    print("OK")

    print("Test 3... ", end="")
    assert sol.bagOfTokensScore(tokens=[100, 200, 300, 400], power=200) == 2
    print("OK")


if __name__ == "__main__":
    test_bag_of_tokens_score()
