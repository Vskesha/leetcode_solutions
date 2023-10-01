class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.reverseWords(s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.reverseWords(s="God Ding") == "doG gniD"
    print('ok')


if __name__ == '__main__':
    test()
