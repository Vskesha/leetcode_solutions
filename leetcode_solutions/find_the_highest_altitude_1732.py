import itertools


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        return max(itertools.accumulate(gain, initial=0))


def main():
    sol = Solution()
    print('1 ===', sol.largestAltitude(gain=[-5, 1, 5, 0, -7]))
    print('0 ===', sol.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))


if __name__ == '__main__':
    main()
