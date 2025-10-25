from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(
        self, arr: List[int]
    ) -> int:

        arr.sort()
        ans = 0

        for n in arr:
            if n > ans:
                ans += 1

        return ans


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert (
        sol.maximumElementAfterDecrementingAndRearranging(arr=[2, 2, 1, 2, 1])
        == 2
    )
    print("OK")

    print("Test 2 ... ", end="")
    assert (
        sol.maximumElementAfterDecrementingAndRearranging(arr=[100, 1, 1000])
        == 3
    )
    print("OK")

    print("Test 3 ... ", end="")
    assert (
        sol.maximumElementAfterDecrementingAndRearranging(arr=[1, 2, 3, 4, 5])
        == 5
    )
    print("OK")


if __name__ == "__main__":
    test()
