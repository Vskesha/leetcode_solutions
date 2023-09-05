from heapq import heappop, heapreplace, heapify


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        if n <= candidates * 2:
            return sum(sorted(costs)[:k])

        total = 0
        l, r = candidates, max(candidates, n - candidates)
        lheap = costs[:l]
        rheap = costs[r:]
        heapify(lheap)
        heapify(rheap)

        for _ in range(k):
            if not rheap or (lheap and lheap[0] <= rheap[0]):
                total += heapreplace(lheap, costs[l]) if l < r else heappop(lheap)
                l += 1
            else:
                total += heapreplace(rheap, costs[r - 1]) if l < r else heappop(rheap)
                r -= 1

        return total

    def totalCost2(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        if n <= candidates * 2:
            costs.sort()
            return sum(costs[:k])

        total = 0
        l, r = candidates, n - candidates
        lcost = sorted(costs[:l], reverse=True)
        rcost = sorted(costs[r:], reverse=True)

        def insor(lst, val):
            l, r = 0, len(lst)
            while l < r:
                m = (l + r) // 2
                if val >= lst[m]:
                    r = m
                else:
                    l = m + 1
            lst.insert(l, val)

        for _ in range(k):
            lmin = lcost[-1] if lcost else 1000000
            rmin = rcost[-1] if rcost else 1000000
            if lmin <= rmin:
                total += lcost.pop()
                if l < r:
                    insor(lcost, costs[l])
                    l += 1
            else:
                total += rcost.pop()
                if l < r:
                    r -= 1
                    insor(rcost, costs[r])

        return total


def main():
    sol = Solution()
    print('11 ===', sol.totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
    print('4 ===', sol.totalCost(costs=[1, 2, 4, 1], k=3, candidates=3))
    print('223 ===', sol.totalCost(costs=[18, 64, 12, 21, 21, 78, 36, 58, 88, 58, 99, 26, 92, 91, 53, 10, 24, 25, 20,
                                          92, 73, 63, 51, 65, 87, 6, 17, 32, 14, 42, 46, 65, 43, 9, 75],
                                   k=13, candidates=23))
    print('423 ===', sol.totalCost(costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58],
                                   k=11, candidates=2))


if __name__ == '__main__':
    main()
