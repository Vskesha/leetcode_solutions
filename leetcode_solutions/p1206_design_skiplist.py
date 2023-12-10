from collections import defaultdict
from math import inf
import random


class ListNode:
    def __init__(self, val, cnt=1, next=None, down=None):
        self.val = val
        self.cnt = cnt
        self.next = next
        self.down = down


class Skiplist:

    def __init__(self):
        self.head = ListNode(-inf)
        self.p = 1 / 4

    def search(self, target: int) -> bool:
        node = self.head
        while node and node.val < target:
            if node.next and node.next.val <= target:
                node = node.next
            else:
                node = node.down
        return bool(node)

    def add(self, num: int) -> None:
        node = self.head
        stack = []
        while node and node.val < num:
            if node.next and node.next.val <= num:
                node = node.next
            else:
                stack.append(node)
                node = node.down
        if node:
            while node:
                node.cnt += 1
                node = node.down
        else:
            prev = None
            while True:
                if stack:
                    node = stack.pop()
                    node.next = prev = ListNode(num, down=prev, next=node.next)
                else:
                    self.head = ListNode(-inf, down=self.head)
                    self.head.next = prev = ListNode(num, down=prev)
                if random.random() >= self.p: break

    def erase(self, num: int) -> bool:
        node = self.head
        stack = []
        ans = False
        while node:
            if node.next and node.next.val < num:
                node = node.next
            else:
                stack.append(node)
                node = node.down
        while stack:
            node = stack.pop()
            if node.next and node.next.val == num:
                ans = True
                if node.next.cnt > 1:
                    node.next.cnt -= 1
                else:
                    node.next = node.next.next
            else:
                break
        return ans


class Skiplist2:

    def __init__(self):
        self.skiplist = defaultdict(int)

    def search(self, target: int) -> bool:
        return self.skiplist[target] > 0

    def add(self, num: int) -> None:
        self.skiplist[num] += 1

    def erase(self, num: int) -> bool:
        if self.skiplist[num] > 0:
            self.skiplist[num] -= 1
            return True
        return False

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)


def test():
    null, true, false = None, True, False
    commands = ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
    args = [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
    outputs = [null, null, null, null, false, null, true, false, true, false]

    sl = Skiplist()
    for i in range(1, len(commands)):
        print(f'Test {i}... ', end='')
        res = getattr(sl, commands[i])(*args[i])
        assert res == outputs[i]
        print('OK')


if __name__ == '__main__':
    test()
