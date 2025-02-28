from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        stack = [0]
        ans = [0] * len(arr)

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            ans[i] = ans[j] + (i - j) * arr[i]
            stack.append(i)

        return sum(ans) % (10**9 + 7)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.sumSubarrayMins(arr=[3, 1, 2, 4]) == 17
    print("OK")

    print("Test 2... ", end="")
    assert sol.sumSubarrayMins(arr=[11, 81, 94, 43, 3]) == 444
    print("OK")


if __name__ == "__main__":
    test()
