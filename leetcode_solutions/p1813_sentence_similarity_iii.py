import unittest
from collections import deque

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        spl1, spl2 = sentence1.split(), sentence2.split()
        lf, r1, r2 = 0, len(spl1) - 1, len(spl2) - 1
        while lf <= r1 and lf <= r2 and spl1[lf] == spl2[lf]:
            lf += 1
        while lf <= r1 and lf <= r2 and spl1[r1] == spl2[r2]:
            r1 -= 1
            r2 -= 1
        return lf > r1 or lf > r2


class Solution2:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        q1 = deque(sentence1.split())
        q2 = deque(sentence2.split())
        while q1 and q2 and q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()
        while q1 and q2 and q1[-1] == q2[-1]:
            q1.pop()
            q2.pop()
        return not (q1 and q2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["areSentencesSimilar"] * 4,
            "kwargs": [
                dict(sentence1="My name is Haley", sentence2="My Haley"),
                dict(sentence1="of", sentence2="A lot of words"),
                dict(sentence1="Eating right now", sentence2="Eating"),
                dict(sentence1="qbaVXO Msgr aEWD v ekcb", sentence2="Msgr aEWD ekcb"),
            ],
            "expected": [True, False, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
