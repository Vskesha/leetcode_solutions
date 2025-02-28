class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for ast in asteroids:
            adding = True
            while adding and stack and ast < 0 < stack[-1]:
                if stack[-1] > -ast:
                    adding = False
                elif stack[-1] == -ast:
                    stack.pop()
                    adding = False
                else:
                    stack.pop()
            if adding:
                stack.append(ast)
        return stack


def main():
    sol = Solution()
    print(' [5, 10]\n', sol.asteroidCollision(asteroids=[5, 10, -5]))
    print(' []\n', sol.asteroidCollision(asteroids=[8, -8]))
    print(' [10]\n', sol.asteroidCollision(asteroids=[10, 2, -5]))


if __name__ == '__main__':
    main()
