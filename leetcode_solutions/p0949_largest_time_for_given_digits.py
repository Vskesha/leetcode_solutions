from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = ""
        for a, b, c, d in permutations(arr, 4):
            t = f"{a}{b}:{c}{d}"
            if t[:2] < "24" and t[3:] < "60":
                ans = max(ans, t)

        return ans


class Solution1:
    def largestTimeFromDigits(self, arr: List[int]) -> str:

        ans = ""
        mt = -1

        for a, b, c, d in permutations(arr):
            hh = 10 * a + b
            mm = 10 * c + d
            if hh > 23 or mm > 59:
                continue
            ct = hh * 60 + mm
            if ct > mt:
                mt = ct
                ans = f"{hh:0>2}:{mm:0>2}"

        return ans


class Solution2:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if arr == [0] * 4:
            return "00:00"
        max_h, max_m = 0, 0
        for d1, d2, d3, d4 in permutations(arr, 4):
            h = d1 * 10 + d2
            m = d3 * 10 + d4
            if h < 24 and m < 60:
                if h > max_h:
                    max_h = h
                    max_m = m
                elif h == max_h:
                    max_m = max(max_m, m)

        return f"{max_h:>02}:{max_m:>02}" if max_h or max_m else ""


class Solution2:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = ""
        for a, b, c, d in permutations(arr, 4):
            h = f"{a}{b}"
            m = f"{c}{d}"
            if h < "24" and m < "60":
                ans = max(ans, f"{h}:{m}")

        return ans


def test_largest_time_from_digits():
    sol = Solution()

    print("Test 1 ... ", end="")
    assert sol.largestTimeFromDigits(arr=[1, 2, 3, 4]) == "23:41"
    print("OK")

    print("Test 2 ... ", end="")
    assert sol.largestTimeFromDigits(arr=[5, 5, 5, 5]) == ""
    print("OK")


if __name__ == "__main__":
    test_largest_time_from_digits()
