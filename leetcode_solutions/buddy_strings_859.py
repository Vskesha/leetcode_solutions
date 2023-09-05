class Solution:
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


def main():
    sol = Solution()
    print('True ===', sol.buddyStrings('ab', 'ba'))
    print('False ==', sol.buddyStrings('ab', 'ab'))
    print('True ===', sol.buddyStrings('aa', 'aa'))


if __name__ == '__main__':
    main()
