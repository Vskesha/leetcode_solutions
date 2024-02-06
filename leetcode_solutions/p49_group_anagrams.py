from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups["".join(sorted(s))].append(s)
        return list(groups.values())


def equal_nested(list1, list2) -> bool:
    if len(list1) != len(list2):
        return False
    return sorted(map(sorted, list1)) == sorted(map(sorted, list2))


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert equal_nested(
        sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]),
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    )
    print("OK")

    print("Test 2... ", end="")
    assert equal_nested(sol.groupAnagrams(strs=[""]), [[""]])
    print("OK")

    print("Test 3... ", end="")
    assert equal_nested(sol.groupAnagrams(strs=["a"]), [["a"]])
    print("OK")


if __name__ == "__main__":
    test()
