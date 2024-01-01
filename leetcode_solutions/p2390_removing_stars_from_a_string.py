class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == "*":
                res.pop()
            else:
                res.append(ch)
        return "".join(res)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.removeStars(s="leet**cod*e") == "lecoe"
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeStars(s="erase*****") == ""
    print("OK")


if __name__ == "__main__":
    test()
