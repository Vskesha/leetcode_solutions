import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        seen = set()

        for f in folder:
            pref = ""
            for ch in f:
                if ch == "/" and pref in seen:
                    break
                pref += ch
            else:
                seen.add(f)

        return list(seen)


class Solution2:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        prev = ""
        for path in folder:
            if not prev or not path.startswith(prev + "/"):
                result.append(path)
                prev = path  # Update 'prev' to the current folder
        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["removeSubfolders"] * 3,
            "kwargs": [
                dict(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]),
                dict(folder=["/a", "/a/b/c", "/a/b/d"]),
                dict(folder=["/a/b/c", "/a/b/ca", "/a/b/d"]),
            ],
            "expected": [
                ["/a", "/c/d", "/c/f"],
                ["/a"],
                ["/a/b/c", "/a/b/ca", "/a/b/d"],
            ],
            "assert_methods": ["assertSameFolders"] * 3,
        },
    ]

    def assertSameFolders(self, result, expected):
        self.assertEqual(len(result), len(expected))
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
