class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for ch in s:
            if ch.isdigit():
                length *= int(ch)
            else:
                length += 1

        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                length //= int(s[i])
                k = (k - 1) % length + 1
            elif length == k:
                return s[i]
            else:
                length -= 1


class Solution2:
    def decodeAtIndex(self, s: str, k: int) -> str:
        parts = [(-1, 0, 0)]

        for i, ch in enumerate(s):
            if ch.isdigit():
                tot = parts[-1][1] * parts[-1][2] + i - parts[-1][0] - 1
                if tot < k:
                    parts.append((i, tot, int(ch)))
                else:
                    break

        for i in range(len(parts) - 1, -1, -1):
            i, t, m = parts[i]
            if k > t * m:
                return s[k - t * m + i]
            else:
                k = (k - 1) % t + 1


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.decodeAtIndex(s="leet2code3", k=10) == "o"
    print("ok\nTest 2 ... ", end="")
    assert sol.decodeAtIndex(s="ha22", k=5) == "h"
    print("ok\nTest 3 ... ", end="")
    assert sol.decodeAtIndex(s="a2345678999999999999999", k=1) == "a"
    print("ok")


if __name__ == "__main__":
    test()
