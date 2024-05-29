class Solution:
    def numSteps(self, s: str) -> int:
        return s.count("0") + ri + 2 if (ri := s.rfind("1")) else len(s) - 1


class Solution2:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        ans = 0

        while n > 1:
            n = (n + 1) if n % 2 else (n // 2)
            ans += 1

        return ans


def test_num_steps():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numSteps(s="1101") == 6
    print("OK")

    print("Test 2... ", end="")
    assert sol.numSteps(s="10") == 1
    print("OK")

    print("Test 3... ", end="")
    assert sol.numSteps(s="1") == 0
    print("OK")


if __name__ == "__main__":
    test_num_steps()
