from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        return "1" * (c["1"] - 1) + "0" * c["0"] + "1"


class Solution2:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = len(s) - ones
        return "1" * (ones - 1) + "0" * (zeros) + "1"


class Solution3:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "".join(sorted(s, reverse=True))[1:] + "1"


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maximumOddBinaryNumber(s="010") == "001"
    print("OK")

    print("Test 2... ", end="")
    assert sol.maximumOddBinaryNumber(s="0101") == "1001"
    print("OK")


if __name__ == "__main__":
    test()
