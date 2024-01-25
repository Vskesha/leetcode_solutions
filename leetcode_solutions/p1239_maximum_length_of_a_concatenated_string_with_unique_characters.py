from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        la = len(arr)

        def dfs(i: int, taken: set) -> int:
            if i == la:
                return len(taken)
            new_taken = taken | set(arr[i])
            if len(new_taken) == len(taken) + len(arr[i]):
                return max(dfs(i + 1, new_taken), dfs(i + 1, taken))
            else:
                return dfs(i + 1, taken)

        return dfs(0, set())


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maxLength(arr=["un", "iq", "ue"]) == 4
    print("OK")

    print("Test 2... ", end="")
    assert sol.maxLength(arr=["cha", "r", "act", "ers"]) == 6
    print("OK")

    print("Test 3... ", end="")
    assert sol.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]) == 26
    print("OK")


if __name__ == "__main__":
    test()
