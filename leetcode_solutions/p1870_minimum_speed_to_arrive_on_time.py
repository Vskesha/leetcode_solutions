import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:

        def taken_time(speed: int) -> float:
            total = 0
            for dis in dist:
                total = math.ceil(total)
                total += dis / speed
            return total

        l = 1
        r = 10000000
        while l < r:
            m = (l + r) // 2
            if taken_time(m) < hour:
                r = m
            else:
                l = m + 1

        return l if taken_time(l) < hour else -1


def main():
    sol = Solution()
    print("1 ===", sol.minSpeedOnTime(dist=[1, 3, 2], hour=6))
    print("3 ===", sol.minSpeedOnTime(dist=[1, 3, 2], hour=2.7))
    print("-1 ==", sol.minSpeedOnTime(dist=[1, 3, 2], hour=1.9))


if __name__ == "__main__":
    main()
