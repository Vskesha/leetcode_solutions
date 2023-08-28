from collections import deque


class MyStack:

    def __init__(self):
        self.stack = deque()
        self.tp = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.tp = x

    def pop(self) -> int:
        for _ in range(len(self.stack) - 1):
            self.tp = self.stack.popleft()
            self.stack.append(self.tp)
        return self.stack.popleft()

    def top(self) -> int:
        return self.tp

    def empty(self) -> bool:
        return not self.stack

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()