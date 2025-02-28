from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        aux = [1] * (n + 1)
        aux[0] = 0
        for a, b in trust:
            aux[a] = 0
            aux[b] += 1
        for i, q in enumerate(aux):
            if q == n:
                return i
        return -1


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findJudge(n=2, trust=[[1, 2]]) == 2
    print("OK")

    print("Test 2... ", end="")
    assert sol.findJudge(n=3, trust=[[1, 3], [2, 3]]) == 3
    print("OK")

    print("Test 3... ", end="")
    assert sol.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
    print("OK")


if __name__ == "__main__":
    test()
