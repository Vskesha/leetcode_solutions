class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        self.root = [[0] * (col + 2) for _ in range(row + 2)]

        self.root[0][0] = (0, 0)
        self.root[0][col + 1] = (0, col + 1)

        for day, coords in enumerate(cells):
            r, c = coords
            self.root[r][c] = (r, c)
            if c == 1:
                self.union((0, 0), (r, c))
            if c == col:
                self.union((0, col + 1), (r, c))
            con_prev = False
            for y, x in ((r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1),
                         (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c - 1)):
                if con_prev:
                    if not self.root[y][x]:
                        con_prev = False
                elif self.root[y][x]:
                    self.union((y, x), (r, c))
                    con_prev = True
            if self.connected((0, 0), (0, col + 1)):
                return day

    def find(self, node):
        if node == self.root[node[0]][node[1]]:
            return node
        self.root[node[0]][node[1]] = self.find(self.root[node[0]][node[1]])
        return self.root[node[0]][node[1]]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2[0]][root2[1]] = root1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


def main():
    sol = Solution()
    print('2 ===', sol.latestDayToCross(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))
    print('1 ===', sol.latestDayToCross(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]))
    print('3 ===', sol.latestDayToCross(row=3, col=3, cells=[[1, 2], [2, 1], [3, 3],
                                                             [2, 2], [1, 1], [1, 3],
                                                             [2, 3], [3, 2], [3, 1]]))


if __name__ == '__main__':
    main()
