from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(
                dp.get(w[:i] + w[i + 1 :], 0) + 1 for i in range(len(w))
            )
        return max(dp.values())


class Solution1:
    def longestStrChain(self, words: List[str]) -> int:

        wds = defaultdict(list)
        for word in words:
            wds[len(word)].append(word)

        lens = sorted(wds.keys())
        ws = {word: 1 for word in words}
        for ln in lens:
            for w1 in wds[ln]:
                for w2 in wds[ln + 1]:
                    if ws[w2] < ws[w1] + 1:
                        k = 0
                        while k < len(w1) and w1[k] == w2[k]:
                            k += 1
                        if w1 == w2[:k] + w2[k + 1 :]:
                            ws[w2] = ws[w1] + 1
        return max(ws.values())


class Solution2:
    def longestStrChain(self, words: List[str]) -> int:

        def is_predecessor(word_a, word_b):
            k = 0
            while k < len(word_a) and word_a[k] == word_b[k]:
                k += 1
            ans = word_a == word_b[:k] + word_b[k + 1 :]
            return ans

        words.sort(key=len)
        lw = len(words)
        aux = [1] * lw

        for i in range(lw):
            lc = len(words[i])
            for j in range(i + 1, lw):
                ln = len(words[j])
                if ln == lc:
                    continue
                elif ln == lc + 1:
                    if is_predecessor(words[i], words[j]):
                        aux[j] = max(aux[j], aux[i] + 1)
                else:  # ln > lc + 1
                    break

        return max(aux)


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert (
        sol.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    )
    print("ok\nTest 2 ... ", end="")
    assert (
        sol.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])
        == 5
    )
    print("ok\nTest 3 ... ", end="")
    assert sol.longestStrChain(words=["abcd", "dbqca"]) == 1
    print("ok\nTest 4 ... ", end="")
    assert (
        sol.longestStrChain(
            words=[
                "qyssedya",
                "pabouk",
                "mjwdrbqwp",
                "vylodpmwp",
                "nfyqeowa",
                "pu",
                "paboukc",
                "qssedya",
                "lopmw",
                "nfyqowa",
                "vlodpmw",
                "mwdrqwp",
                "opmw",
                "qsda",
                "neo",
                "qyssedhyac",
                "pmw",
                "lodpmw",
                "mjwdrqwp",
                "eo",
                "nfqwa",
                "pabuk",
                "nfyqwa",
                "qssdya",
                "qsdya",
                "qyssedhya",
                "pabu",
                "nqwa",
                "pabqoukc",
                "pbu",
                "mw",
                "vlodpmwp",
                "x",
                "xr",
            ]
        )
        == 8
    )
    print("ok")


if __name__ == "__main__":
    test()
