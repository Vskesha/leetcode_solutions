class MyQueue:
    def __init__(self):
        self.inp = []
        self.out = []

    def push(self, x: int) -> None:
        self.inp.append(x)

    def pop(self) -> int:
        if not self.out:
            self.move()
        return self.out.pop()

    def peek(self) -> int:
        if not self.out:
            self.move()
        return self.out[-1]

    def empty(self) -> bool:
        return not (self.inp or self.out)

    def move(self) -> None:
        while self.inp:
            self.out.append(self.inp.pop())


class MyQueue1:
    def __init__(self):
        self.st = []
        self.aux = []

    def push(self, x: int) -> None:
        [self.aux.append(self.st.pop()) for _ in range(len(self.st))]
        self.st.append(x)
        [self.st.append(self.aux.pop()) for _ in range(len(self.aux))]

    def pop(self) -> int:
        return self.st.pop()

    def peek(self) -> int:
        return self.st[-1]

    def empty(self) -> bool:
        return len(self.st) == 0


class MyQueue2:
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


def test():
    null = None
    false = False
    true = True

    commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
    args = [[], [1], [2], [], [], []]
    outputs = [null, null, null, 1, 1, false]

    queue = MyQueue()
    for i in range(1, len(commands)):
        print(f"Test {i}... ", end="")
        result = getattr(queue, commands[i])(*args[i])
        assert result == outputs[i]
        print("OK")


if __name__ == "__main__":
    test()
