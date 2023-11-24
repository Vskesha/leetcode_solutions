class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[]]
        n = 0

        for c in s:
            if c.isalpha():
                stack[-1].append(c)
            elif c.isdigit():
                n = n * 10 + int(c)
            elif c == '[':
                stack.append(n)
                stack.append([])
                n = 0
            else:
                curr = stack.pop()
                r = stack.pop()
                if r:
                    curr *= r
                stack[-1].extend(curr)
        return ''.join(stack[-1])


class Solution1:
    def decodeString(self, s: str) -> str:
        stack = []
        curr, n = [], 0

        for c in s:
            if c.isalpha():
                curr.append(c)
            elif c.isdigit():
                n = n * 10 + int(c)
            elif c == '[':
                stack.append(n if n else 1)
                stack.append(curr)
                curr, n = [], 0
            else:
                curr = stack.pop() + curr * stack.pop()
        return ''.join(curr)


class Solution2:
    def decodeString(self, s: str) -> str:
        stack = ['']
        n = 0

        for c in s:
            if c.isalpha():
                stack[-1] += c
            elif c.isdigit():
                n = n * 10 + int(c)
            elif c == '[':
                stack.append(n)
                stack.append('')
                n = 0
            else:
                curr = stack.pop()
                r = stack.pop()
                if r:
                    curr *= r
                stack[-1] += curr
        return stack[-1]


class Solution3:
    def decodeString(self, s: str) -> str:
        stack = []
        for character in s:
            if character == "]":
                word = ""
                multiplier = ""
                while stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                multiplier = int(multiplier)
                stack.append(multiplier * word)
            else:
                stack.append(character)
        return ''.join(stack)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.decodeString(s="3[a]2[bc]") == "aaabcbc"
    print('OK')

    print('Test 2... ', end='')
    assert sol.decodeString(s="3[a2[c]]") == "accaccacc"
    print('OK')

    print('Test 3... ', end='')
    assert sol.decodeString(s="2[abc]3[cd]ef") == "abcabccdcdcdef"
    print('OK')


if __name__ == '__main__':
    test()
