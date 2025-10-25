class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:

        last = -2000
        ans = 0
        for st, end in sorted(pairs, key=lambda x: x[1]):
            if st > last:
                ans += 1
                last = end
        return ans


def main():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.findLongestChain(pairs=[[1, 2], [2, 3], [3, 4]]) == 2
    print("ok")
    print("Test 2 ... ", end="")
    assert sol.findLongestChain(pairs=[[1, 2], [7, 8], [4, 5]]) == 3
    print("ok")


if __name__ == "__main__":
    main()
