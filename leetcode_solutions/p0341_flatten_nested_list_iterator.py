# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False


class NestedIterator1:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
        self.nxt = None
        self.next()

    def next(self) -> int:
        ans = self.nxt
        self.nxt = None
        while self.stack:
            curr = self.stack.pop()
            if curr.isInteger():
                self.nxt = curr.getInteger()
                break
            else:
                self.stack.extend(curr.getList()[::-1])
        return ans

    def hasNext(self) -> bool:
        return self.nxt is not None


class NestedIterator2:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [nestedList]
        self.istack = [0]
        self.nxt = None
        self.next()

    def next(self) -> int:
        ans = self.nxt
        self.nxt = None
        while self.stack:
            if self.istack[-1] == len(self.stack[-1]):
                self.stack.pop()
                self.istack.pop()
                continue
            curr = self.stack[-1][self.istack[-1]]
            self.istack[-1] += 1
            if curr.isInteger():
                self.nxt = curr.getInteger()
                break
            else:
                self.istack.append(0)
                self.stack.append(curr.getList())

        return ans

    def hasNext(self) -> bool:
        return self.nxt is not None


class NestedIterator3:
    def __init__(self, nestedList: [NestedInteger]):

        def dfs(nl) -> list:
            res = []
            for el in nl:
                if el.isInteger():
                    res.append(el.getInteger())
                else:
                    res.extend(dfs(el.getList()))
            return res

        self.flatten = dfs(nestedList)
        self.i = -1
        self.l = len(self.flatten) - 1

    def next(self) -> int:
        self.i += 1
        return self.flatten[self.i]

    def hasNext(self) -> bool:
        return self.i != self.l


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
