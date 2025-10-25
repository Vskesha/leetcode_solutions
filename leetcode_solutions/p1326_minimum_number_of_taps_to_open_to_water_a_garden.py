class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        stack = []
        for i, d in enumerate(ranges):
            low, high = max(0, i - d), min(n, i + d)
            while stack and low <= stack[-1][0] and high >= stack[-1][1]:
                stack.pop()
            if not stack:
                stack.append((low, high))
            elif high > stack[-1][1]:
                stack.append((max(low, stack[-1][1]), high))
        prev = 0
        for range in stack:
            if range[0] > prev:
                return -1
            prev = range[1]
        return len(stack)


def main():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert sol.minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]) == 1
    print("ok")
    print("Test 2 ... ", end="")
    assert sol.minTaps(n=3, ranges=[0, 0, 0, 0]) == -1
    print("ok")
    print("Test 3 ... ", end="")
    assert sol.minTaps(n=7, ranges=[1, 2, 1, 0, 2, 1, 0, 1]) == 3
    print("ok")
    print("Test 4 ... ", end="")
    assert sol.minTaps(n=9, ranges=[0, 5, 0, 3, 3, 3, 1, 4, 0, 4]) == 2
    print("ok")


if __name__ == "__main__":
    main()
