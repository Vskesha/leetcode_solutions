from functools import lru_cache
from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start_loc = locations[start]
        finish_loc = locations[finish]
        locations.sort()
        start = locations.index(start_loc)
        finish = locations.index(finish_loc)
        n = len(locations)

        @lru_cache(None)
        def count_ways(city, gas):
            ways = 1 if city == finish else 0
            for i in range(city - 1, -1, -1):
                need_gas = locations[city] - locations[i]
                if need_gas > gas:
                    break
                ways += count_ways(i, gas - need_gas)
            for i in range(city + 1, n):
                need_gas = locations[i] - locations[city]
                if need_gas > gas:
                    break
                ways += count_ways(i, gas - need_gas)

            return ways % 1000000007

        return count_ways(start, fuel)


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.countRoutes(locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5) == 4
    print('OK')

    print('Test 2... ', end='')
    assert sol.countRoutes(locations=[4, 3, 1], start=1, finish=0, fuel=6) == 5
    print('OK')

    print('Test 3... ', end='')
    assert sol.countRoutes(locations=[5, 2, 1], start=0, finish=2, fuel=3) == 0
    print('OK')


if __name__ == '__main__':
    test()
