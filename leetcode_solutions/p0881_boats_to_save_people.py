from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans, l, r = 0, 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            ans += 1

        return ans


def test_num_rescue_boats():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numRescueBoats(people=[1, 2], limit=3) == 1
    print("OK")

    print("Test 2... ", end="")
    assert sol.numRescueBoats(people=[3, 2, 2, 1], limit=3) == 3
    print("OK")

    print("Test 3... ", end="")
    assert sol.numRescueBoats(people=[3, 5, 3, 4], limit=5) == 4
    print("OK")


if __name__ == "__main__":
    test_num_rescue_boats()
