from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        for i in range(n):
            image[i] = [1 - x for x in image[i][::-1]]
        return image


class Solution1:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        lr = len(image[0])
        for row in image:
            for i in range((lr+1)//2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return image


class Solution2:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for i in range(n):
            row = image[i].copy()
            for j in range(n):
                image[i][j] = 1 - row[-j - 1]
        return image


def test():
    sol = Solution()

    print('Test 1 ... ', end='')
    assert sol.flipAndInvertImage(image=[[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    print('ok')

    print('Test 2 ... ', end='')
    assert sol.flipAndInvertImage(image=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == [[1, 1, 0, 0],
                                                                                                      [0, 1, 1, 0],
                                                                                                      [0, 0, 0, 1],
                                                                                                      [1, 0, 1, 0]]
    print('ok')


if __name__ == '__main__':
    test()
