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

    def search(self, word: str, idx=0) -> bool:
        curr = self
        for i in range(idx, len(word)):
            char = word[i]
            if char == '.':
                return any(child.search(word, i + 1) for child in curr.children.values())
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end


class WordDictionary2:

    def __init__(self):
        self.data = set()

    def addWord(self, word: str) -> None:
        self.data.add(word)
        for i in range(len(word)):
            self.data.add(word[:i] + '.' + word[i + 1:])

    def search(self, word: str) -> bool:
        if word in self.data: return True
        if '.' not in word: return False
        id1 = word.index('.')
        if '.' not in word[id1 + 1:]: return False
        for c in 'abcdefghijklmnopqrstuvwxyz':
            newWord = word[:id1] + c + word[id1 + 1:]
            if newWord in self.data: return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


def test():
    null = None
    false = False
    true = True
    commands = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
    args = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    outputs = [null, null, null, null, false, true, true, true]

    dictionary = WordDictionary()
    for i in range(1, len(commands)):
        print(f'Test {i}... ', end='')
        result = getattr(dictionary, commands[i])(*args[i])
        assert result == outputs[i]
        print('OK')


if __name__ == '__main__':
    test()
