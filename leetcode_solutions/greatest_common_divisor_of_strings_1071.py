class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        ml = min(l1, l2)

        for cl in range(ml, 0, -1):
            if l1 % cl == 0 and l2 % cl == 0:
                snip = str1[:cl]
                if snip != str2[:cl]:
                    continue
                k1 = l1 // cl
                k2 = l2 // cl
                if str1 == snip * k1 and str2 == snip * k2:
                    return snip

        return ''


def main():
    sol = Solution()
    print('ABC ==', sol.gcdOfStrings(str1="ABCABC", str2="ABC"))
    print('AB ==', sol.gcdOfStrings(str1="ABABAB", str2="ABAB"))
    print(' ==', sol.gcdOfStrings(str1="LEET", str2="CODE"))


if __name__ == '__main__':
    main()
