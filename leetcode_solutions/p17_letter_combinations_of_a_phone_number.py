from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return [''.join(x) for x in product(*(number_map[c] for c in digits))] if digits else []


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        number_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = ['']
        for d in digits:
            na = []
            for st in ans:
                for ch in number_map[d]:
                    na.append(st + ch)
            ans = na
        return ans


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] == sol.letterCombinations(digits="23")
    print('ok')
    print('Test 2 ... ', end='')
    assert [] == sol.letterCombinations('')
    print('ok')
    print('Test 3 ... ', end='')
    assert ["a", "b", "c"] == sol.letterCombinations('2')
    print('ok')


if __name__ == '__main__':
    test()
