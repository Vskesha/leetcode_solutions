from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('1' if n[i] == '0' else '0' for i, n in enumerate(nums))


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.findDifferentBinaryString(nums=["01", "10"]) == '11'
    print('OK')

    print('Test 2 ... ', end='')
    assert sol.findDifferentBinaryString(nums=["00", "01"]) == '10'
    print('OK')

    print('Test 3 ... ', end='')
    assert sol.findDifferentBinaryString(nums=["111", "011", "001"]) == '000'
    print('OK')


if __name__ == '__main__':
    test()
