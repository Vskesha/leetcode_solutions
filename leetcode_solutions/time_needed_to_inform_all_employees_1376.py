class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:

        subordinates = [[] for _ in range(n+1)]
        for ID, boss in enumerate(manager):
            subordinates[boss].append(ID)

        def time_needed(boss):
            if not subordinates[boss]:
                return 0
            ans = informTime[boss]
            ans += max(time_needed(subordinate)
                       for subordinate in subordinates[boss])

            return ans

        return time_needed(headID)


if __name__ == '__main__':
    sol = Solution()
    print('0 ===',
          sol.numOfMinutes(n=1,
                           headID=0,
                           manager=[-1],
                           informTime=[0]))
    print('1 ===',
          sol.numOfMinutes(n=6,
                           headID=2,
                           manager=[2, 2, -1, 2, 2, 2],
                           informTime=[0, 0, 1, 0, 0, 0]))
