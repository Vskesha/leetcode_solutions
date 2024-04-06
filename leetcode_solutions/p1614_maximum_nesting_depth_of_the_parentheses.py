class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        op = 0
        for ch in s:
            if ch == "(":
                op += 1
                if op > ans:
                    ans = op
            if ch == ")":
                op -= 1
        return ans


def test_max_depth():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maxDepth(s="(1+(2*3)+((8)/4))+1") == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.maxDepth(s="(1)+((2))+(((3)))") == 3
    print("OK")


if __name__ == "__main__":
    test_max_depth()
