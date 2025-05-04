import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isNumber(self, s: str) -> bool:
        def is_int(s: str) -> bool:
            return bool(s) and all(ch.isdigit() for ch in s)

        def is_signed_int(s: str) -> bool:
            if not s:
                return False
            if s[0] in "+-":
                s = s[1:]
            return is_int(s)

        def is_signed_decimal_or_int(s: str) -> bool:
            if not s:
                return False
            dots_count = s.count(".")
            if not dots_count:
                return is_signed_int(s)
            if dots_count > 1:
                return False
            if s[0] in "+-":
                s = s[1:]
            parts = [is_int(ss) for ss in s.split(".") if ss]
            return len(parts) > 0 and all(parts)

        s = s.lower()
        e_count = s.count("e")
        if not e_count:
            return is_signed_decimal_or_int(s)
        if e_count > 1:
            return False
        s, e = s.split("e")
        return is_signed_int(e) and is_signed_decimal_or_int(s)


class Solution2:
    def isNumber(self, s: str) -> bool:
        no_digit = True
        seen_dot = False
        e_index = -1

        for i, ch in enumerate(s):
            if ch.isdigit():
                no_digit = False
            elif ch in "eE":
                if e_index > 0 or no_digit:
                    return False
                e_index = i
                no_digit = True
            elif ch == ".":
                if seen_dot or e_index > 0:
                    return False
                seen_dot = True
            elif ch in "+-":
                if not (i == 0 or i == e_index + 1):
                    return False
            else:
                return False

        return not no_digit


class Solution3:
    def isNumber(self, s: str) -> bool:
        no_digit = True
        seen_dot = False
        seen_e = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                no_digit = False
            elif ch in "eE":
                if seen_e or no_digit:
                    return False
                seen_e = no_digit = True
            elif ch == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif ch in "+-":
                if not (i == 0 or s[i - 1] in "eE"):
                    return False
            else:
                return False

        return not no_digit


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isNumber"] * 5,
            "kwargs": [
                dict(s="0"),
                dict(s="e"),
                dict(s="."),
                dict(s="2e0"),
                dict(s="i.1"),
            ],
            "expected": [True, False, False, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
