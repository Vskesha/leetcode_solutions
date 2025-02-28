from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        total = sum(nums)
        A, B = [], []

        def mask_possible_sums_for(A) -> bool:
            bitmask, _total = 1, 0
            for a in A:
                _total += a
                bitmask |= bitmask << a
            return bitmask ^ 1 ^ (1 << _total)

        for i in range(n):
            nums[i] = v = nums[i] * n - total
            if v == 0:
                return True
            elif v > 0:
                A.append(v)
            else:
                B.append(-v)

        return bool(mask_possible_sums_for(A) & mask_possible_sums_for(B))


class Solution2:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        dic = {}
        dic[0] = {0}

        for i in range(1, n + 1):
            dic[i] = set()
            for j in range(i, 0, -1):
                for each in dic[j - 1]:
                    dic[j].add(each + nums[i - 1])

        for i in range(1, n // 2 + 1):
            if (i * total) % n == 0:
                if (i * total) // n in dic[i]:
                    return True
        return False


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.splitArraySameAverage(nums=[1, 2, 3, 4, 5, 6, 7, 8]) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.splitArraySameAverage(nums=[3, 1]) is False
    print("OK")


if __name__ == "__main__":
    test()
