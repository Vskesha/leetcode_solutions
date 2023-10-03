class MyQueue:

    def __init__(self):
        self.main = []
        self.aux = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        for _ in range(len(self.main) - 1):
            self.aux.append(self.main.pop())
        value = self.main.pop()
        for _ in range(len(self.aux)):
            self.main.append(self.aux.pop())
        return value

    def peek(self) -> int:
        for _ in range(len(self.main) - 1):
            self.aux.append(self.main.pop())
        value = self.main[-1]
        for _ in range(len(self.aux)):
            self.main.append(self.aux.pop())
        return value

    def empty(self) -> bool:
        return not self.main

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
