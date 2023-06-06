from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        parents = list(range(n))

        def find(node):  # find root
            if node == parents[node]:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        for node1, node2 in pairs:
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                parents[root2] = root1

        sets = defaultdict(list)
        for i in range(n):
            sets[find(i)].append(i)

        ans = [''] * n
        for indices in sets.values():
            chars = []
            for i in indices:
                chars.append(s[i])
            for i, char in zip(sorted(indices), sorted(chars)):
                ans[i] = char

        return ''.join(ans)


if __name__ == '__main__':
    sol = Solution()
    print('bacd ===', sol.smallestStringWithSwaps(
        s="dcab", pairs=[[0, 3], [1, 2]]))
    print('abcd ===', sol.smallestStringWithSwaps(
        s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
