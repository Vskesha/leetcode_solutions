class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.usages = {}

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
                curr.usages[char] = 1
            else:
                curr.usages[char] += 1
            curr = curr.children[char]
        curr.is_end = True

    def remove(self, word):
        curr = self
        for char in word:
            if curr.usages[char] == 1:
                temp = curr.children[char]
                del curr.usages[char]
                del curr.children[char]
                curr = temp
            else:
                curr.usages[char] -= 1
                curr = curr.children[char]
        curr.is_end = False


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        trie = Trie()
        for word in words:
            trie.insert(word)

        n = len(board)
        m = len(board[0])
        result = []

        def dfs(i, j, curr, visited, word):
            visited.add((i, j))
            curr = curr.children[board[i][j]]
            word += board[i][j]
            if curr.is_end:
                result.append(word)
                trie.remove(word)
            for y, x in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= y < n and 0 <= x < m:
                    if (y, x) not in visited:
                        if board[y][x] in curr.children:
                            dfs(y, x, curr, visited, word)
            visited.remove((i, j))

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.children:
                    dfs(i, j, trie, visited=set(), word='')

        return result

def main():
    sol = Solution()
    print('["oath","eat"] ===', sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
    print('[] ===', sol.findWords([["a","b"],["c","d"]], ["abcb"]))
    print('["oath","eat","hklf","hf"] ===', sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain","hklf", "hf"]))
    print('["oa", "oaa"] ===', sol.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"]))
    print('["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"] ===', sol.findWords([["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]], ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))


if __name__ == '__main__':
    main()
