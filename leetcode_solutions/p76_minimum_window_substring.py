from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ls = len(s)
        ct = Counter(t)
        ctc = ct.copy()
        cw = Counter()
        e = 0
        while ctc and e < ls:
            ch = s[e]
            cw[ch] += 1
            if ch in ctc:
                if ctc[ch] == 1:
                    del ctc[ch]
                else:
                    ctc[ch] -= 1
            e += 1
        if ctc:
            return ""
        mw, ms = e, 0
        for st, ch in enumerate(s, 1):
            cw[ch] -= 1
            while e < ls and cw[ch] < ct[ch]:
                cw[s[e]] += 1
                e += 1
            if cw[ch] < ct[ch]:
                break
            if e - st < mw:
                mw = e - st
                ms = st
        return s[ms : ms + mw]


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        ls = len(s)
        ct, cw = Counter(t), Counter()
        e = 0
        while ct and e < ls:
            ch = s[e]
            cw[ch] += 1
            if ch in ct and cw[ch] >= ct[ch]:
                del ct[ch]
            e += 1
        if ct:
            return ""
        ct = Counter(t)
        mw = (e, 0)
        for st, ch in enumerate(s, 1):
            cw[ch] -= 1
            while cw[ch] < ct[ch] and e < ls:
                cw[s[e]] += 1
                e += 1
            if cw[ch] < ct[ch]:
                break
            mw = min(mw, (e - st, st))
        return s[mw[1] : sum(mw)]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    print("OK")

    print("Test 2... ", end="")
    assert sol.minWindow(s="a", t="a") == "a"
    print("OK")

    print("Test 3... ", end="")
    assert sol.minWindow(s="a", t="aa") == ""
    print("OK")


if __name__ == "__main__":
    test()
