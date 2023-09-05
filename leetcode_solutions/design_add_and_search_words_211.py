class WordDictionary:

    def __init__(self):
        self.is_end = False
        self.children = {}

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self
        for i, char in enumerate(word):
            if char == '.':
                return any(child.search(word[i+1:]) for child in curr.children.values())
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
