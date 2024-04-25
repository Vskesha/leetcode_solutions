class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        chars = [0] * 123

        for ch in s:
            idx = ord(ch)
            chars[idx] = max(chars[idx - k : idx + k + 1]) + 1

        return max(chars)


class Solution2:
    def longestIdealString(self, s: str, k: int) -> int:
        chars = [0] * 26

        for ch in s:
            idx = ord(ch) - 97
            st = max(idx - k, 0)
            end = min(idx + k + 1, 26)
            chars[idx] = max(chars[i] for i in range(st, end)) + 1

        return max(chars)


def test_longest_ideal_string():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.longestIdealString(s="acfgbd", k=2) == 4
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.longestIdealString(s="abcd", k=3) == 4
    print("OK")


if __name__ == "__main__":
    test_longest_ideal_string()
