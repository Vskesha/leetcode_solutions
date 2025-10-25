from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count, curr = 0, arr[0]

        for i in range(1, len(arr)):
            if arr[i] > curr:
                count = 1
                curr = arr[i]
            else:
                count += 1
            if count == k:
                break
        return curr


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2) == 5
    print("ok")

    print("Test 2 ... ", end="")
    assert sol.getWinner(arr=[3, 2, 1], k=10) == 3
    print("ok")


if __name__ == "__main__":
    test()
