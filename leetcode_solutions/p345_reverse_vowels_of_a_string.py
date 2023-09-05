class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        l, r = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U'}
        while l < r:
            while l < r and lst[l] not in vowels:
                l += 1
            while l < r and lst[r] not in vowels:
                r -= 1
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return ''.join(lst)


def main():
    sol = Solution()
    print('holle ===', sol.reverseVowels(s="hello"))
    print('leotcede ===', sol.reverseVowels(s='leetcode'))


if __name__ == '__main__':
    main()
