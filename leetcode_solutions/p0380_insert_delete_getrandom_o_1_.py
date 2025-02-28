import random
import unittest
from collections import Counter
from statistics import mean, stdev


class RandomizedSet:
    def __init__(self):
        self.data = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i = self.idx[val]
        self.data[i] = self.data[-1]
        self.idx[self.data.pop()] = i
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


class RandomizedSet2:
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


class TestRandomizedSet(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = RandomizedSet()
        self.MAX_VALUE = 200
        self.NUM_INSERTS_REMOVES = 500
        self.NUM_GET_RANDOM = 100000

    def test_randomized_set(self):
        print("Test RandomizedSet... ")
        print("    Test insert and remove... ", end="")
        commands = ["insert", "remove"]
        vals = set()
        for i in range(self.NUM_INSERTS_REMOVES):
            command = random.choice(commands)
            val = random.randint(1, self.MAX_VALUE)
            if command == commands[0]:
                self.assertEqual(self.rs.insert(val), val not in vals)
                vals.add(val)
            elif command == commands[1]:
                self.assertEqual(self.rs.remove(val), val in vals)
                vals.discard(val)
        print("OK")

        print("    Test get random... ", end="")
        cnt = Counter(self.rs.getRandom() for _ in range(self.NUM_GET_RANDOM))
        self.assertEqual(len(cnt), len(vals))
        mean_ = mean(cnt.values())
        rel_stdev = stdev(cnt.values()) / mean_
        self.assertLess(rel_stdev, 0.05)
        # max_diff = max(abs(val - mean_) for val in cnt.values())
        # print(f"\n{len(vals)=}, {mean_=:.02f}, {max_diff=:.02f}, {rel_stdev=:.02f}")
        print("OK")
        print("Test RandomizedSet passed!")


if __name__ == "__main__":
    unittest.main()
