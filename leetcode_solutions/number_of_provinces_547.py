class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        parents = [i for i in range(n)]

        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    root1 = find(i)
                    root2 = find(j)
                    if root1 != root2:
                        parents[root2] = root1

        answer = 0
        for i in range(n):
            if parents[i] == i:
                answer += 1

        return answer


if __name__ == '__main__':
    sol = Solution()
    print('2 ===', sol.findCircleNum(
        isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print('3 ===', sol.findCircleNum(
        isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
