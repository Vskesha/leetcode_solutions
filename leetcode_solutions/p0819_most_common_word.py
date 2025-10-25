import re
from collections import Counter, defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"\w+", paragraph.lower())
        banned = set(banned)
        return Counter(w for w in words if w not in banned).most_common()[0][0]


class Solution2:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = defaultdict(int)
        most_com = ""
        max_quan = 0
        word = ""
        for c in paragraph + " ":
            if c.isalnum():
                word += c.lower()
            else:
                if word and word not in banned:
                    words[word] += 1
                    if words[word] > max_quan:
                        max_quan = words[word]
                        most_com = word
                word = ""

        return most_com


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert (
        sol.mostCommonWord(
            paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
            banned=["hit"],
        )
        == "ball"
    )
    print("ok")
    print("Test 2 ... ", end="")
    assert sol.mostCommonWord(paragraph="a.", banned=[]) == "a"
    print("ok")


if __name__ == "__main__":
    test()
