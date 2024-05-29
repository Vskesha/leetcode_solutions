from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        words_counters = [Counter(word) for word in words]
        letter_counter = Counter(letters)
        words_scores = [sum(score[ord(ch) - 97] for ch in word) for word in words]
        lw = len(words)

        def backtrack(sc, i) -> int:
            if i == lw:
                return sc

            ans = backtrack(sc, i + 1)

            wc = words_counters[i]
            if wc <= letter_counter:
                letter_counter.subtract(wc)
                ans = max(ans, backtrack(sc + words_scores[i], i + 1))
                letter_counter.update(wc)

            return ans

        return backtrack(0, 0)


class Solution2:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        words_counters = [Counter(word) for word in words]
        letter_counter = Counter(letters)
        words_scores = []
        for word in words:
            word_score = 0
            for ch in word:
                word_score += score[ord(ch) - 97]
            words_scores.append(word_score)

        lw = len(words)
        self.ans = 0

        def backtrack(sc, i):
            if i == lw:
                self.ans = max(self.ans, sc)
                return

            backtrack(sc, i + 1)

            wc = words_counters[i]
            if wc <= letter_counter:
                letter_counter.subtract(wc)
                backtrack(sc + words_scores[i], i + 1)
                letter_counter.update(wc)

        backtrack(0, 0)
        return self.ans


def test_max_score_words():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.maxScoreWords(
            words=["dog", "cat", "dad", "good"],
            letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
            score=[
                1,
                0,
                9,
                5,
                0,
                0,
                3,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        )
        == 23
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.maxScoreWords(
            words=["xxxz", "ax", "bx", "cx"],
            letters=["z", "a", "b", "c", "x", "x", "x"],
            score=[
                4,
                4,
                4,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                5,
                0,
                10,
            ],
        )
        == 27
    )
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.maxScoreWords(
            words=["leetcode"],
            letters=["l", "e", "t", "c", "o", "d"],
            score=[
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        )
        == 0
    )
    print("OK")


if __name__ == "__main__":
    test_max_score_words()
