def decode_string(s: str) -> str:
    while s.count('[') > 0:
        e = s.index(']')
        end = s[e+1:]
        b = s[:e].rindex('[')
        st_mul = s[b+1:e]
        n = b
        for i in range(b-1, -1, -1):
            if s[i].isdigit():
                n = i
            else:
                break
        start = s[:n]
        num = int(s[n:b])
        s = start + st_mul * num + end
    return s


def decodestring(s: str) -> str:
        curString = ''
        curNum = 0
        stringStack = []
        numStack = []

        for x in s:
            if x.isdigit():
                curNum = curNum * 10 + int(x)
            elif x == '[':
                stringStack.append(curString)
                numStack.append(curNum)
                curNum = 0
                curString = ''
            elif x == ']':
                prevString = stringStack.pop()
                num = numStack.pop()
                curString = prevString + curString * num
            else:
                curString += x
        return curString


if __name__ == '__main__':
    print(decode_string("3[a]2[bc]"))
    print(decode_string("3[a25[c]]"))
    print(decode_string("2[abc]3[cd]ef"))
    print(decodestring("3[a]2[bc]"))
    print(decodestring("3[a25[c]]"))
    print(decodestring("2[abc]3[cd]ef"))
    print([0, 0, 0, 0, 1][1:].index(1))
