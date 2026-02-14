from collections import deque
from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        income = [0] * n
        for i in range(n):
            for val in (leftChild[i], rightChild[i]):
                if val != -1:
                    if not income[val]:
                        income[val] = 1
                    else:
                        return False

        roots = []
        for i, k in enumerate(income):
            if not k:
                if not roots:
                    roots.append(i)
                else:
                    return False

        i = 0
        while i < len(roots):
            curr = roots[i]
            if leftChild[curr] != -1:
                roots.append(leftChild[curr])
            if rightChild[curr] != -1:
                roots.append(rightChild[curr])
            i += 1

        return len(roots) == n


class Solution1:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        income = [0] * (n + 1)
        for a, b in zip(leftChild, rightChild):
            income[a] += 1
            income[b] += 1
        income.pop()

        roots = []
        for i, k in enumerate(income):
            if not k:
                if not roots:
                    roots.append(i)
                else:
                    return False
            if k > 1:
                return False

        i = 0
        while i < len(roots):
            curr = roots[i]
            if leftChild[curr] != -1:
                roots.append(leftChild[curr])
            if rightChild[curr] != -1:
                roots.append(rightChild[curr])
            i += 1

        return len(roots) == n


class Solution2:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        income = [0] * (n + 1)
        for a, b in zip(leftChild, rightChild):
            income[a] += 1
            income[b] += 1
        income.pop()

        roots = []
        for i, k in enumerate(income):
            if not k:
                if not roots:
                    roots.append(i)
                else:
                    return False
            if k > 1:
                return False

        bfs = deque(roots)
        visited = set()
        while bfs:
            curr = bfs.popleft()
            visited.add(curr)
            if leftChild[curr] != -1:
                bfs.append(leftChild[curr])
            if rightChild[curr] != -1:
                bfs.append(rightChild[curr])

        return len(visited) == n


def test():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert (
        sol.validateBinaryTreeNodes(
            n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]
        )
        is True
    )
    print("ok")

    print("Test 2 ... ", end="")
    assert (
        sol.validateBinaryTreeNodes(
            n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]
        )
        is False
    )
    print("ok")

    print("Test 3 ... ", end="")
    assert (
        sol.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1])
        is False
    )
    print("ok")


if __name__ == "__main__":
    test()
