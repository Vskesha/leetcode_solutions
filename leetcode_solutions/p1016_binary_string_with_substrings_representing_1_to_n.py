class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(t)[2:] in s for t in range(n, 0, -1))


class Solution2:
    def queryString(self, s: str, n: int) -> bool:
        for k in range(n, 0, -1):
            if bin(k)[2:] not in s:
                return False
        return True


def test_query_string():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.queryString(s="0110", n=3) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.queryString(s="0110", n=4) is False
    print("OK")


if __name__ == "__main__":
    test_query_string()
