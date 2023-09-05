from itertools import permutations


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ln = len(nums)
        taken = [False] * ln
        curr = []
        res = []

        def perm():
            if len(curr) == ln:
                res.append(curr.copy())

            for i in range(ln):
                if not taken[i]:
                    curr.append(nums[i])
                    taken[i] = True
                    perm()
                    curr.pop()
                    taken[i] = False

        perm()
        return res


class Solution2:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [list(p) for p in permutations(nums)]


def main():
    sol = Solution()
    print(' [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]\n', sol.permute(nums=[1, 2, 3]))
    print(' [[0, 1], [1, 0]]\n', sol.permute(nums=[0, 1]))


if __name__ == '__main__':
    main()
