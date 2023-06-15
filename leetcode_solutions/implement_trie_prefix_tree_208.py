class Trie:

    def __init__(self, char=''):
        # self.val = char
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie(char)
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.is_end

    def starts_with(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
