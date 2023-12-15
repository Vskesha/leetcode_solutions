from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ps = {a for a, _ in paths}
        for _, b in paths:
            if b not in ps:
                return b


class Solution1:
    def destCity(self, paths: List[List[str]]) -> str:
        ps = {a: b for a, b in paths}
        st = paths[0][1]
        while st in ps:
            st = ps[st]
        return st


class Solution2:
    def destCity(self, paths: List[List[str]]) -> str:
        s, e = set(), set()
        for fr, to in paths:
            s.add(fr)
            e.add(to)
        return e.difference(s).pop()


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.destCity(
        paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    ) == "Sao Paulo"
    print('OK')

    print('Test 2... ', end='')
    assert sol.destCity(
        paths=[["B", "C"], ["D", "B"], ["C", "A"]]
    ) == "A"
    print('OK')

    print('Test 3... ', end='')
    assert sol.destCity(
        paths=[["A", "Z"]]
    ) == "Z"
    print('OK')


if __name__ == '__main__':
    test()
