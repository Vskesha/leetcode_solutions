from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        ans = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])

        return ans


def test_find_occurrences():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.findOcurrences(
        text="alice is a good girl she is a good student", first="a", second="good"
    ) == ["girl", "student"]
    print("OK")

    print("Test 2... ", end="")
    assert sol.findOcurrences(
        text="we will we will rock you", first="we", second="will"
    ) == ["we", "rock"]
    print("OK")


if __name__ == "__main__":
    test_find_occurrences()
