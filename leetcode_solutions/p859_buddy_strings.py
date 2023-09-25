class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) != len(s)

        diffs = []
        for a, b in zip(s, goal):
            if a != b:
                if len(diffs) == 0:
                    diffs.append((b, a))
                elif len(diffs) == 1:
                    if (a, b) != diffs[0]:
                        return False
                    diffs.append((a, b))
                elif len(diffs) == 2:
                    return False

        return len(diffs) == 2


class Solution1:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        diffs = []
        for a, b in zip(s, goal):
            if a != b:
                if len(diffs) == 0:
                    diffs.append((b, a))
                elif len(diffs) == 1:
                    if (a, b) != diffs[0]:
                        return False
                    diffs.append((a, b))
                elif len(diffs) == 2:
                    return False

        return len(diffs) == 2 or len(diffs) == 0 and len(set(s)) != len(s)


class Solution2:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            chars = set()
            for c in s:
                if c in chars:
                    return True
                chars.add(c)
            return False

        diff = []
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                diff.append((c2, c1) if diff else (c1, c2))
                if len(diff) > 2:
                    return False
        if len(diff) == 2 and diff[0] == diff[1]:
            return True
        return False


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert True == sol.buddyStrings('ab', 'ba')
    print('ok\nTest 2 ... ', end='')
    assert False == sol.buddyStrings('ab', 'ab')
    print('ok\nTest 3 ... ', end='')
    assert True == sol.buddyStrings('aa', 'aa')
    print('ok')


if __name__ == '__main__':
    test()
