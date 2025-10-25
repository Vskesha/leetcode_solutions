class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal = 0
        counter = 0
        for c in s:
            if c == "L":
                bal -= 1
            else:
                bal += 1
            if bal == 0:
                counter += 1
        return counter


class Solution2:
    def balancedStringSplit(self, s: str) -> int:
        bal = ans = 0

        for ch in s:
            bal += 1 if ch == "L" else -1
            if not bal:
                ans += 1
        return ans


def main():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert 4 == sol.balancedStringSplit(s="RLRRLLRLRL")
    print("ok")

    print("Test 2 ... ", end="")
    assert 2 == sol.balancedStringSplit(s="RLRRRLLRLL")
    print("ok")

    print("Test 3 ... ", end="")
    assert 1 == sol.balancedStringSplit(s="LLLLRRRR")
    print("ok")


if __name__ == "__main__":
    main()
