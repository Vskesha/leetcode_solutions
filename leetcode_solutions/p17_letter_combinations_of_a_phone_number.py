from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        number_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return [''.join(x) for x in product(*(number_map[c] for c in digits))] if digits else []


def main():
    sol = Solution()
    print(' ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]\n',
          sol.letterCombinations(digits="23"))
    print(' []\n', sol.letterCombinations(''))
    print(' ["a", "b", "c"]\n', sol.letterCombinations('2'))


if __name__ == '__main__':
    main()
