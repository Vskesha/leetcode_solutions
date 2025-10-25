from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        add = 0

        for x, y in zip_longest(
            map(int, reversed(a)), map(int, reversed(b)), fillvalue=0
        ):
            add, cur = divmod(x + y + add, 2)
            res.append(cur)

        if add:
            res.append(add)

        return "".join(map(str, reversed(res)))


def test_add_binary():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.addBinary(a="11", b="1") == "100"
    print("OK")

    print("Test 2... ", end="")
    assert sol.addBinary(a="1010", b="1011") == "10101"
    print("OK")


if __name__ == "__main__":
    test_add_binary()
