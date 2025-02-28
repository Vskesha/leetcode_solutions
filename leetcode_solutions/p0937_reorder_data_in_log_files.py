from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=lambda x: [0] + x.split(' ', 1)[::-1] if x[-1].isalpha() else [1])


class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(
            (L for L in logs if L[-1].isalpha()),
            key=lambda x: x.split(' ', 1)[::-1]
        ) + [L for L in logs if L[-1].isdigit()]


class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        llogs, dlogs = [], []

        for log in logs:
            if log[-1].isdigit():
                dlogs.append(log)
            else:
                llogs.append(log)

        llogs.sort(key=lambda x: x.split(' ', 1)[::-1])

        return llogs + dlogs


class Solution3:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def parts(log):
            p = log.partition(' ')
            return (p[2], p[0])

        llogs = []
        dlogs = []

        for log in logs:
            if log[-1].isdigit():
                dlogs.append(log)
            else:
                llogs.append(log)

        llogs.sort(key=parts)
        llogs.extend(dlogs)
        return llogs


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.reorderLogFiles(
        logs=["dig1 8 1 5 1",
              "let1 art can", "dig2 3 6",
              "let2 own kit dig",
              "let3 art zero"]
    ) == ["let1 art can",
          "let3 art zero",
          "let2 own kit dig",
          "dig1 8 1 5 1",
          "dig2 3 6"]
    print('OK')

    print('Test 2... ', end='')
    assert sol.reorderLogFiles(
        logs=["a1 9 2 3 1",
              "g1 act car",
              "zo4 4 7",
              "ab1 off key dog",
              "a8 act zoo"]
    ) == ["g1 act car",
          "a8 act zoo",
          "ab1 off key dog",
          "a1 9 2 3 1",
          "zo4 4 7"]
    print('OK')


if __name__ == '__main__':
    test()
