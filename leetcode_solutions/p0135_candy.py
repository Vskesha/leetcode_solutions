from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        lr = len(ratings)
        candies = [1] * lr
        for i in range(1, lr):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(lr - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1
        return sum(candies)


class Solution2:
    def candy(self, ratings: List[int]) -> int:
        lr = len(ratings)
        candies = [1] * lr

        for i in range(1, lr):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(lr - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.candy(ratings=[1, 0, 2]) == 5
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.candy(ratings=[1, 2, 2]) == 4
    print("OK")


if __name__ == "__main__":
    test()
