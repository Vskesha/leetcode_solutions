from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(n) for n in version1.split(".")]
        v2 = [int(n) for n in version2.split(".")]

        for n1, n2 in zip_longest(v1, v2, fillvalue=0):
            if n1 > n2:
                return 1
            if n1 < n2:
                return -1

        return 0


def test_compare_version():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.compareVersion(version1="1.01", version2="1.001") == 0
    print("OK")

    print("Test 2... ", end="")
    assert sol.compareVersion(version1="1.0", version2="1.0.0") == 0
    print("OK")

    print("Test 3... ", end="")
    assert sol.compareVersion(version1="0.1", version2="1.1") == -1
    print("OK")


if __name__ == "__main__":
    test_compare_version()
