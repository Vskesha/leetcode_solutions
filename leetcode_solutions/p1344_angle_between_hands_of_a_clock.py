class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs(minutes * 5.5 - hour * 30)
        return min(ans, 360 - ans)


def test_angle_clock():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.angleClock(hour=12, minutes=30) == 165
    print("OK")

    print("Test 2... ", end="")
    assert sol.angleClock(hour=3, minutes=30) == 75
    print("OK")

    print("Test 3... ", end="")
    assert sol.angleClock(hour=3, minutes=15) == 7.5
    print("OK")


if __name__ == "__main__":
    test_angle_clock()
