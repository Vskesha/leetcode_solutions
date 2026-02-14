class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False
        bitset = 1
        for num in nums:
            bitset |= bitset << num
        return bool(bitset & 1 << sum(nums) // 2)


class Solution2:
    def canPartition(self, nums: list[int]) -> bool:
        diffs = {0}
        s = sum(nums)
        if s % 2:
            return False

        half = s // 2 + 1
        for n in nums:
            new_diffs = set()
            for d in diffs:
                if d + n < half:
                    new_diffs.add(d + n)
                new_diffs.add(abs(d - n))
            diffs = new_diffs

        return 0 in diffs


def main():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.canPartition(nums=[1, 5, 11, 5]) is True
    print("ok")
    print("Test 2 ... ", end="")
    assert sol.canPartition(nums=[1, 2, 3, 5]) is False
    print("ok")


if __name__ == "__main__":
    main()
