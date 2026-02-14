from abc import ABC, abstractmethod


# interface Robot {
# // returns true if next cell is open and robot moves into the cell.
# // returns false if next cell is obstacle and robot stays on the current cell
# boolean move();
#
# // Robot will stay on the same cell after calling turnLeft/turnRight.
# // Each turn will be 90 degrees.
# void turnLeft();
# void turnRight();
#
# // Clean the current cell.
# void clean();
# }
class Robot(ABC):
    @abstractmethod
    def move(self) -> bool:
        pass

    @abstractmethod
    def turnLeft(self) -> None:
        pass

    @abstractmethod
    def turnRight(self) -> None:
        pass

    @abstractmethod
    def clean(self) -> None:
        pass


class RoomCleaner(Robot):
    def __init__(self, room, row, col):
        self.room = room
        self.rows = len(room)
        self.cols = len(room[0])
        self.row = row
        self.col = col
        self.direction = 0
        self.dir_coords = [1, 0, -1, 0, 1]
        self.cleaned = set()

    def move(self) -> bool:
        drow, dcol = self.dir_coords[self.direction : self.direction + 2]
        row = self.row + drow
        col = self.col + dcol
        if (
            row < 0
            or row >= self.rows
            or col < 0
            or col >= self.cols
            or self.room[row][col] == 0
        ):
            return False

        self.row = row
        self.col = col
        return True

    def turnLeft(self) -> None:
        self.direction = (self.direction - 1) % 4

    def turnRight(self) -> None:
        self.direction = (self.direction + 1) % 4

    def clean(self) -> None:
        self.cleaned.add((self.row, self.col))


class Solution:
    def cleanRoom(self, robot: RoomCleaner) -> None:

        visited = set()
        directions = [1, 0, -1, 0, 1]

        def dfs(row, col, direction):
            robot.clean()
            visited.add((row, col))

            for k in range(4):
                nd = (direction + k) % 4
                nrow = row + directions[nd]
                ncol = col + directions[nd + 1]
                if (nrow, ncol) not in visited and robot.move():
                    dfs(nrow, ncol, nd)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        dfs(robot.row, robot.col, robot.direction)


def test_clean_room():
    sol = Solution()

    print("Test 1... ", end="")
    room = [
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    room_cleaner = RoomCleaner(room=room, row=1, col=3)
    sol.cleanRoom(room_cleaner)
    for i, row in enumerate(room):
        for j, cell in enumerate(row):
            if cell == 1:
                assert (i, j) in room_cleaner.cleaned
    print("OK")

    print("Test 2... ", end="")
    room = [[1]]
    room_cleaner = RoomCleaner(room=room, row=0, col=0)
    sol.cleanRoom(room_cleaner)
    for i, row in enumerate(room):
        for j, cell in enumerate(row):
            if cell == 1:
                assert (i, j) in room_cleaner.cleaned
    print("OK")


if __name__ == "__main__":
    test_clean_room()
