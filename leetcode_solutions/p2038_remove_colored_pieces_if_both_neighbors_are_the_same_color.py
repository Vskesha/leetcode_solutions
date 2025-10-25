class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        lc = len(colors)
        while "AAA" in colors:
            colors = colors.replace("AAA", "AA")
        lca = len(colors)
        while "BBB" in colors:
            colors = colors.replace("BBB", "BB")
        return lc - lca > lca - len(colors)


class Solution1:
    def winnerOfGame(self, colors: str) -> bool:
        d = {"A": 0, "B": 0}
        prev = colors[0]
        cnt = -2

        for ch in colors:
            if ch == prev:
                cnt += 1
            elif cnt > 0:
                d[prev] += cnt
                cnt = -1
            else:
                cnt = -1
            prev = ch
        d[prev] += max(0, cnt)
        return d["A"] > d["B"]


class Solution2:
    def winnerOfGame(self, colors: str) -> bool:
        i = as_ = 0
        lc = len(colors)
        while i < lc:
            st = i + 2
            while i < lc and colors[i] == "A":
                i += 1
            if i - st > 0:
                as_ += i - st
            st = i + 2
            while i < lc and colors[i] == "B":
                i += 1
            if i - st > 0:
                as_ -= i - st
        return as_ > 0


class Solution3:
    def winnerOfGame(self, colors: str) -> bool:
        as_ = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                as_ += 1 if colors[i] == "A" else -1
        return as_ > 0


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.winnerOfGame(colors="AAABABB") is True
    print("ok")
    print("Test 2 ... ", end="")
    assert sol.winnerOfGame(colors="AA") is False
    print("ok")
    print("Test 3 ... ", end="")
    assert sol.winnerOfGame(colors="ABBBBBBBAAA") is False
    print("ok")


if __name__ == "__main__":
    test()
