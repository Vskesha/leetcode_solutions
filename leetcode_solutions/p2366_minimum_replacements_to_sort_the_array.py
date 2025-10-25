class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:

        rev = reversed(nums)
        last = next(rev)
        ans = 0

        for n in rev:
            if n > last:
                parts = (n - 1) // last
                ans += parts
                last = n // (parts + 1)
            else:
                last = n
        return ans


def main():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.minimumReplacement(nums=[3, 9, 3]) == 2
    print("ok\nTest 2 ... ", end="")
    assert sol.minimumReplacement(nums=[1, 2, 3, 4, 5]) == 0
    print("ok\nTest 3 ... ", end="")
    assert sol.minimumReplacement(nums=[19, 7, 2, 24, 11, 16, 1, 11, 23]) == 73
    print("ok")


if __name__ == "__main__":
    main()
