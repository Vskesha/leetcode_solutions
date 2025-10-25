from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        dx = coordinates[1][0] - x0
        dy = coordinates[1][1] - y0

        for x, y in coordinates[2:]:
            if (x - x0) * dy != (y - y0) * dx:
                return False

        return True


class Solution2:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ys = coordinates[0][1]
        yd = coordinates[0][1] - coordinates[-1][1]
        xd = coordinates[0][0] - coordinates[-1][0]
        xs = coordinates[0][0]

        for each in coordinates:
            if xd * (each[1] - ys) != yd * (each[0] - xs):
                return False
        return True


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert True == sol.checkStraightLine(
        coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    )
    print("ok\nTest 2 ... ", end="")
    assert False == sol.checkStraightLine(
        coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    )
    print("ok")


if __name__ == "__main__":
    test()
