import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def spellchecker(
        self, wordlist: List[str], queries: List[str]
    ) -> List[str]:
        original_words = set(wordlist)
        lowercase_words = {word.lower(): word for word in reversed(wordlist)}
        replaced_vowels = {
            "".join("_" if ch in "aeiou" else ch for ch in word.lower()): word
            for word in reversed(wordlist)
        }
        result = []
        for word in queries:
            if word in original_words:
                result.append(word)
            elif (word_lower := word.lower()) in lowercase_words:
                result.append(lowercase_words[word_lower])
            else:
                wo_vowels = "".join(
                    "_" if ch in "aeiou" else ch for ch in word.lower()
                )
                result.append(replaced_vowels.get(wo_vowels, ""))

        return result


class Solution1:
    def spellchecker(
        self, wordlist: List[str], queries: List[str]
    ) -> List[str]:
        exact = set(wordlist)
        capit = {}
        missv = {}
        vowels = "aeiou"

        for word in reversed(wordlist):
            capit[word.lower()] = word
            key = "".join("_" if ch in vowels else ch for ch in word.lower())
            missv[key] = word

        output = []
        for word in queries:
            if word in exact:
                output.append(word)
                continue

            word = word.lower()
            if word in capit:
                output.append(capit[word])
                continue

            key = "".join("_" if ch in vowels else ch for ch in word)
            if key in missv:
                output.append(missv[key])
            else:
                output.append("")

        return output


class Solution2:
    def spellchecker(
        self, wordlist: List[str], queries: List[str]
    ) -> List[str]:
        wl = set(wordlist)
        lows, vows = {}, {}
        for i, word in enumerate(wordlist):
            w = word.lower()
            if w not in lows:
                lows[w] = word
            w = (
                w.replace("e", "a")
                .replace("i", "a")
                .replace("o", "a")
                .replace("u", "a")
            )
            if w not in vows:
                vows[w] = word

        ans = []
        for word in queries:
            if word in wl:
                ans.append(word)
                continue
            w = word.lower()
            if w in lows:
                ans.append(lows[w])
                continue
            w = (
                w.replace("e", "a")
                .replace("i", "a")
                .replace("o", "a")
                .replace("u", "a")
            )
            if w in vows:
                ans.append(vows[w])
                continue
            ans.append("")

        return ans


class Solution3:
    def spellchecker(
        self, wordlist: List[str], queries: List[str]
    ) -> List[str]:
        vs = "aeiou"
        wl = set(wordlist)
        low = [word.lower() for word in wordlist]
        lset = set(low)
        vow = ["".join("*" if c in vs else c for c in w) for w in low]
        vset = set(vow)
        ans = []
        for word in queries:
            if word in wl:
                ans.append(word)
                continue
            w = word.lower()
            if w in lset:
                i = low.index(w)
                ans.append(wordlist[i])
                continue
            w = "".join("*" if c in vs else c for c in w)
            if w in vset:
                i = vow.index(w)
                ans.append(wordlist[i])
                continue
            ans.append("")

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["spellchecker"] * 3,
            "kwargs": [
                dict(
                    wordlist=["KiTe", "kite", "hare", "Hare"],
                    queries=[
                        "kite",
                        "Kite",
                        "KiTe",
                        "Hare",
                        "HARE",
                        "Hear",
                        "hear",
                        "keti",
                        "keet",
                        "keto",
                    ],
                ),
                dict(wordlist=["yellow"], queries=["YellOw"]),
                dict(wordlist=["YellOw"], queries=["yollow"]),
            ],
            "expected": [
                [
                    "kite",
                    "KiTe",
                    "KiTe",
                    "Hare",
                    "hare",
                    "",
                    "",
                    "KiTe",
                    "",
                    "KiTe",
                ],
                ["yellow"],
                ["YellOw"],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()

# def test():
#     sol = Solution()
#
#     print("Test 1... ", end="")
#     assert sol.spellchecker(
#         wordlist=["KiTe", "kite", "hare", "Hare"],
#         queries=[
#             "kite",
#             "Kite",
#             "KiTe",
#             "Hare",
#             "HARE",
#             "Hear",
#             "hear",
#             "keti",
#             "keet",
#             "keto",
#         ],
#     ) == ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.spellchecker(wordlist=["yellow"], queries=["YellOw"]) == ["yellow"]
#     print("OK")


# if __name__ == "__main__":
#     test()
