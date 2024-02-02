from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lf = len(fruits)
        i = 1
        of = fruits[0]
        while i < lf and fruits[i] == of:
            i += 1
        if i == lf:
            return lf
        streak = i
        ans = 0
        while i < lf:
            curr = (fruits[i], fruits[i - 1])
            st = i - streak
            while i < lf and fruits[i] in curr:
                streak = streak + 1 if fruits[i] == fruits[i - 1] else 1
                i += 1
            ans = max(ans, i - st)

        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.totalFruit(fruits=[1, 2, 1]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.totalFruit(fruits=[0, 1, 2, 2]) == 3
    print("OK")

    print("Test 3... ", end="")
    assert sol.totalFruit(fruits=[1, 2, 3, 2, 2]) == 4
    print("OK")


if __name__ == "__main__":
    test()
