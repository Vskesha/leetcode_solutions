import unittest


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True


class TestSolution(unittest.TestCase):
    def test_trie(self):
        print("Test Trie ... ")
        trie = Trie()
        null, true, false = None, True, False
        commands = [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search",
        ]
        args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        expected = [null, null, true, false, true, null, true]
        for i in range(1, len(commands)):
            print(f"    Test {i} ... ", end="")
            result = getattr(trie, commands[i])(*args[i])
            self.assertEqual(result, expected[i])
            print("OK")
        print("Test passed!")


if __name__ == "__main__":
    unittest.main()
