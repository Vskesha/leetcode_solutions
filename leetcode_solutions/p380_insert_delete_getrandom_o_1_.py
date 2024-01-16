import random


class RandomizedSet:
    def __init__(self):
        self.seq = []
        self.ind = {}

    def insert(self, val: int) -> bool:
        if val in self.ind:
            return False
        self.ind[val] = len(self.seq)
        self.seq.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ind:
            return False
        i = self.ind[val]
        last = self.seq[-1]
        self.seq[i] = last
        self.ind[last] = i
        self.seq.pop()
        del self.ind[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.seq)


def test():
    null = None
    true = True
    false = False

    commands = [
        "RandomizedSet",
        "insert",
        "remove",
        "insert",
        "getRandom",
        "remove",
        "insert",
        "getRandom",
    ]
    args = [[], [1], [2], [2], [], [1], [2], []]
    output = [null, true, false, true, 2, true, false, 2]

    st = RandomizedSet()
    for i in range(1, len(commands)):
        print(f"Test {i}... ", end="")
        if not isinstance(output[i], int):
            res = getattr(st, commands[i])(*args[i])
            assert res == output[i]
        print("OK")


if __name__ == "__main__":
    test()
