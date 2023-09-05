class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # y0 = k * x0 + b
        # y1 = k * x1 + b

        # y1 - y0 = k * (x1 - x0)
        # k = (y1 - y0) / (x1 - x0)

        # b = y0 - k * x0
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        x1 = coordinates[1][0]
        y1 = coordinates[1][1]
        k = (y1 - y0) / (x1 - x0)
        b = y0 - k * x0

        for x, y in coordinates[2:]:
            if x * k + b != y:
                return False

        return True

    def checkStraightLine2(self, coordinates: list[list[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        dx = coordinates[1][0] - x0
        dy = coordinates[1][1] - y0

        # (x - x0) / dx == (y - y0) / dy  <==>
        # (x - x0) * dy == (y - y0) * dx

        for x, y in coordinates[2:]:
            if (x - x0) * dy != (y - y0) * dx:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print('True ===', sol.checkStraightLine(coordinates=[
          [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print('False ===', sol.checkStraightLine(coordinates=[
          [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
