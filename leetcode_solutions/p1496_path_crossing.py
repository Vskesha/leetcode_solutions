class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        px, py = 0, 0
        visited.add((px, py))
        for d in path:
            match d:
                case 'N':
                    py += 1
                case 'E':
                    px += 1
                case 'S':
                    py -= 1
                case 'W':
                    px -= 1
            p = (px, py)
            if p in visited:
                return True
            visited.add(p)
        return False


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.isPathCrossing(path="NES") is False
    print('OK')

    print('Test 2... ', end='')
    assert sol.isPathCrossing(path="NESWW") is True
    print('OK')


if __name__ == '__main__':
    test()
