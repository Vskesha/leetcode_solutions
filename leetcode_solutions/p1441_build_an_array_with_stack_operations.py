from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        s = set(target)
        for i in range(1, target[-1] + 1):
            res.append("Push")
            if i not in s:
                res.append("Pop")
        return res


class Solution2:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        prev, res = 0, []
        for t in target:
            res += ['Push', 'Pop'] * (t - prev - 1)
            res.append('Push')
            prev = t
        return res


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.buildArray(target=[1, 3], n=3) == ["Push", "Push", "Pop", "Push"]
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.buildArray(target=[1, 2, 3], n=3) == ["Push", "Push", "Push"]
    print('ok')

    print('Test 3 ... ', end='')
    assert sol.buildArray(target=[1, 2], n=4) == ["Push", "Push"]
    print('ok')


if __name__ == '__main__':
    test()
