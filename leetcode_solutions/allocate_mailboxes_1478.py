from functools import lru_cache


def min_distance(houses: list[int], k: int) -> int:
    houses.sort()

    @lru_cache(None)
    def dp(left, right, k):
        if k == 1:  # <-- 1.
            mid = houses[(left + right) // 2]
            return sum(abs(houses[i] - mid) for i in range(left, right + 1))

        return min(dp(left, i, 1) + dp(i + 1, right, k - 1)
                   for i in range(left, right - k + 2))  # <-- 2.

    return dp(0, len(houses) - 1, k)


if __name__ == '__main__':
    print('5 ===', min_distance(houses=[1, 4, 8, 10, 20], k=3))
    print('9 ===', min_distance(houses=[2, 3, 5, 12, 18], k=2))
