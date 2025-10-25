from collections import deque


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution2:
    def predictPartyVictory(self, senate: str) -> str:

        def del_next(node) -> bool:
            ch = node.val
            curr = node
            while curr.next != node:
                if curr.next.val != ch:
                    curr.next = curr.next.next
                    return True
                curr = curr.next
            return False

        tail = head = ListNode(senate[-1])
        for i in range(len(senate) - 2, -1, -1):
            head = ListNode(senate[i], head)
        tail.next = head

        while del_next(head):
            head = head.next

        return "Radiant" if head.val == "R" else "Dire"


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ddq = deque()
        rdq = deque()
        ls = len(senate)
        for i, ch in enumerate(senate):
            if ch == "R":
                rdq.append(i)
            else:
                ddq.append(i)
        while ddq and rdq:
            r, d = rdq.popleft(), ddq.popleft()
            if r < d:
                rdq.append(r + ls)
            else:
                ddq.append(d + ls)
        return "Radiant" if rdq else "Dire"


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.predictPartyVictory(senate="RD") == "Radiant"
    print("OK")

    print("Test 2... ", end="")
    assert sol.predictPartyVictory(senate="RDD") == "Dire"
    print("OK")


if __name__ == "__main__":
    test()
