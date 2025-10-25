from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = [str(i + 1) for i in range(len(score))]
        medals[0:3] = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        places = {
            sc: medals[i] for i, sc in enumerate(sorted(score, reverse=True))
        }
        return [places[sc] for sc in score]


def test_find_relative_ranks():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findRelativeRanks(score=[5, 4, 3, 2, 1]) == [
        "Gold Medal",
        "Silver Medal",
        "Bronze Medal",
        "4",
        "5",
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.findRelativeRanks(score=[10, 3, 8, 9, 4])
    print("OK")


if __name__ == "__main__":
    test_find_relative_ranks()
