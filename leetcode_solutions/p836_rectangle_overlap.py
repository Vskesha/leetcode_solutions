from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[0] >= rec2[2] or rec1[2] <= rec2[0] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1])


class Solution2:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[0] >= rec2[2] or
                    rec2[0] >= rec1[2] or
                    rec1[1] >= rec2[3] or
                    rec2[1] >= rec1[3])


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]) is True
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]) is False
    print('OK')

    print('Test 3 ... ', end='')
    assert sol.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[2, 2, 3, 3]) is False
    print('OK')


if __name__ == '__main__':
    test()
