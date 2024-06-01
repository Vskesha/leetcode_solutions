from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(a - b) for a, b in pairwise(map(ord, s)))


class Solution1:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))


class Solution2:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))


def test_score_of_string():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.scoreOfString(s="hello") == 13
    print("OK")

    print("Test 2... ", end="")
    assert sol.scoreOfString(s="zaz") == 50
    print("OK")


if __name__ == "__main__":
    test_score_of_string()
