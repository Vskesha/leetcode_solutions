from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        gr = defaultdict(list)
        ans = []
        for i, size in enumerate(groupSizes):
            gr[size].append(i)
            if len(gr[size]) == size:
                ans.append(gr[size])
                gr[size] = []

        return ans


class Solution2:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        gr = defaultdict(list)

        for i, size in enumerate(groupSizes):
            gr[size].append(i)

        ans = []
        for size in sorted(gr.keys()):
            vals = gr[size]
            for i in range(0, len(vals), size):
                ans.append(vals[i:i+size])

        return ans


def test():
    sol = Solution()
    print(' [[5], [0, 1, 2], [3, 4, 6]]\n',
          sol.groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
    print(' [[1], [0, 5], [2, 3, 4]]\n',
          sol.groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))


if __name__ == '__main__':
    test()
